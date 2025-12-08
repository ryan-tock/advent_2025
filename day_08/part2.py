import utils
import time

data = utils.fetch_input(day=8)
# data = utils.fetch_small(day=8)
# data = utils.fetch_test(day=8)
benchmark_start = time.time()

lines = data.splitlines()
junctions = [n.split(",") for n in lines]
junctions = [(int(n[0]), int(n[1]), int(n[2])) for n in junctions]

pairs = [
    (junctions[n], junctions[k])
    for n in range(len(junctions) - 1)
    for k in range(n + 1, len(junctions))
]
pairs.sort(
    key=lambda x: (x[0][0] - x[1][0]) ** 2
    + (x[0][1] - x[1][1]) ** 2
    + (x[0][2] - x[1][2]) ** 2
)

networks = [{junction} for junction in junctions]

connections = 0

for pair in pairs:
    network0 = {}
    network1 = {}
    for i, network in enumerate(networks):
        if pair[0] in network:
            network0 = network
        if pair[1] in network:
            network1 = network

    if network0 == network1:
        connections += 1
        continue

    networks.remove(network0)
    networks.remove(network1)

    networks.append(network0.union(network1))
    connections += 1

    if len(networks) == 1:
        print(pair[0][0] * pair[1][0])
        break

print(f"time taken: {(time.time() - benchmark_start):.{4}f}s")
