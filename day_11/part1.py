import utils
import time

data = utils.fetch_input(day=11)
# data = utils.fetch_small(day=11)
# data = utils.fetch_test(day=11)
benchmark_start = time.time()

lines = data.splitlines()
connections = {line.split(": ")[0]: line.split(": ")[1].split(" ") for line in lines}

at = ["you"]

total = 0
while len(at) > 0:
    working = at.pop()

    if working == "out":
        total += 1
        continue

    for connection in connections[working]:
        at.append(connection)

print(total)

print(f"time taken: {(time.time() - benchmark_start):.{4}f}s")
