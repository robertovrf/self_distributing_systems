#!/bin/bash

set -e

pushd "$(dirname "$(readlink -f "$0")")"
kubectl delete --ignore-not-found=true -R -f ../kubernetes/first_experiment/

kubectl apply -f ../kubernetes/rbac/naive.yaml 
kubectl apply -R -f ../kubernetes/first_experiment/

declare -a ips
function get_ips() {
    IN=$(kubectl get svc -l app=remote-dist -o jsonpath='{.items..status.loadBalancer.ingress..ip}')
    IFS=' ' read -a ips <<< "$IN"
}

echo "Waiting for Load Balancers..."
while [ "${#ips[@]}" -lt 2 ]; do
    sleep .5
    get_ips
done

echo "IP1: ${ips[0]}"
echo "IP2: ${ips[1]}"

echo "Updating ListCPSharding.dn"
cd ../../distributor/data/adt/
sed -i '' -e "s#\(const char IP1\[\] =\) \".*\"#\1 \"${ips[0]}\"#g" ListCPSharding.dn
sed -i '' -e "s#\(const char IP2\[\] =\) \".*\"#\1 \"${ips[1]}\"#g" ListCPSharding.dn
echo "ListCPSharding.dn updated successfully!"