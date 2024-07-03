from logging.config import dictConfig
from fastapi import FastAPI, HTTPException
from kubernetes import client, config
from kubernetes.client.exceptions import ApiException
from jinja2 import Environment, PackageLoader
from dataclasses import dataclass
from yaml import dump, safe_load
from src.log_config import log_config
import time
import logging
import json

dictConfig(log_config)
logger = logging.getLogger("implementation-provider")

REMOTE_DIST_POD_PATH = "remote-dist.yaml"
REMOTE_DIST_SERVICE_PATH = "remote-dist-service.yaml"
LABEL_SELECTOR = "app.kubernetes.io/managed-by=implementation-provider"

app = FastAPI()
jinja_env = Environment(loader=PackageLoader("src"))
jinja_env.filters.update({"to_yaml": lambda x: dump(x)})

config.load_config()

k8s_core_v1 = client.CoreV1Api()
k8s_core_v1.delete_collection_namespaced_pod(namespace="default", label_selector=LABEL_SELECTOR)
k8s_core_v1.delete_collection_namespaced_service(namespace="default", label_selector=LABEL_SELECTOR)

@dataclass
class DistributeRequest:
    implementation: str
    replicas: int
    metadata: list[dict]

@dataclass
class DestroyRequest:
    implementation: str

def retrieve_service_ips():
    k8s_core_v1 = client.CoreV1Api()
    services = k8s_core_v1.list_namespaced_service(namespace="default", label_selector=LABEL_SELECTOR)
    replica_ip = [(x.metadata.labels["replica"], x.status.load_balancer.ingress[0].ip) for x in services.items if x.status.load_balancer.ingress]
    return [x[1] for x in sorted(replica_ip, key=lambda x: x[0])]

@app.post("/distribute")
def distribute(request: DistributeRequest):
    logger.info("Distributing implementation %s to %s replicas", request.implementation, str(request.replicas))
    if len(request.metadata) != request.replicas:
        raise HTTPException(status_code=400, detail="Length of metadata should be equal to the number of replicas")

    pod_template = jinja_env.get_template(REMOTE_DIST_POD_PATH)
    service_template = jinja_env.get_template(REMOTE_DIST_SERVICE_PATH)

    k8s_core_v1 = client.CoreV1Api()
    for replica in range(request.replicas):
        env_dict = {"IMPLEMENTATION": request.implementation, **request.metadata[replica]}
        env = [{ "name": key, "value": value if type(value) == str else json.dumps(value) } for key, value in env_dict.items()]

        implementation_name = request.implementation.split("/")[-1]
        pod = pod_template.render(replica=replica, implementation=implementation_name, env=env)
        service = service_template.render(replica=replica, implementation=implementation_name)

        try:
            k8s_core_v1.create_namespaced_pod(body=safe_load(pod), namespace="default")
            k8s_core_v1.create_namespaced_service(body=safe_load(service), namespace="default")
        except ApiException as e:
            if e.status == 409:
                continue

            raise e

    ips = retrieve_service_ips()
    while len(ips) != request.replicas:
        time.sleep(0.25)
        ips = retrieve_service_ips()

    return ips

@app.post("/destroy")
def destroy(request: DestroyRequest):
    k8s_core_v1 = client.CoreV1Api()
    selector = f"{LABEL_SELECTOR},implementation={request.implementation.split("/")[-1]}"
    k8s_core_v1.delete_collection_namespaced_pod(namespace="default", label_selector=selector)
    k8s_core_v1.delete_collection_namespaced_service(namespace="default", label_selector=selector)

    return "OK"
