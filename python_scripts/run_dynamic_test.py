import math
import random
import time
import requests
import matplotlib.pyplot as plt
from random import randint
import pandas as pd
from itertools import cycle

random.seed(2324)

items_to_add = cycle(range(0, 100))

server = "localhost"
distributor_port = 3500

server_url = f"http://{server}:8080"

perception_url = f"http://{server}:{distributor_port}/ucb/perception-data"
composition_url = f"http://{server}:{distributor_port}/ucb/composition"


def get_perception_data() -> float:
    response = requests.get(perception_url)
    if response.content.decode("utf-8") == "NOT FOUND":
        print("Something went wrong!")
        return

    action, average_response_time = response.content.decode("utf-8").split("|")
    print(f"Action {action} with average response time {average_response_time}")
    return float(average_response_time)


def set_composition(index):
    requests.post(composition_url, data=str(index))


def run_requests(n: int):
    for _ in range(n):
        requests.post(server_url, data=str(next(items_to_add)))


def delete_elements(n: int):
    for _ in range(n):
        requests.delete(server_url, data=str(randint(101, 200)))


shard_increase = 2000
number_of_increases = 5
resolution = 10
test_requests = 10
request_count = (shard_increase * number_of_increases) // resolution
composition_change = shard_increase // resolution

set_composition(4)
time.sleep(40)

shards = 1
rows = []
print("Starting requests")
for j in range(1, request_count):
    run_requests(resolution)
    get_perception_data()
    delete_elements(test_requests)
    item_count = j * resolution
    response_time = get_perception_data()
    rows.append((item_count, shards, response_time))

    next_shards = shards
    if item_count >= 9000:
        next_shards = 8
    elif item_count >= 6000:
        next_shards = 4
    elif item_count >= 2000:
        next_shards = 2

    if next_shards != shards:
        print("Changing composition")
        shards = next_shards
        rows.append((item_count, shards, response_time))
        set_composition(0)
        set_composition(4)
        time.sleep(40)


df = pd.DataFrame(rows, columns=["item_count", "shards", "response_time"])
df.to_csv("response_times_dynamic.csv", index=False, header=True)

df["response_time"] = df["response_time"].rolling(window=3).min()
df.pivot(index="item_count", columns="shards", values="response_time").plot(
    xlim=(0, 10000),
    ylim=(0, 60),
    figsize=(10, 6.5),
    fontsize=12
)
plt.xlabel("Número de items", fontsize=16, labelpad=12)
plt.ylabel("Tempo de resposta (ms)", fontsize=16, labelpad=12)
plt.show()
