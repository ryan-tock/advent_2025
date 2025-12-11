import utils
import time
import random

data = utils.fetch_input(day=11)
# data = utils.fetch_small(day=11)
# data = utils.fetch_test(day=11)
benchmark_start = time.time()

lines = data.splitlines()
connections = {line.split(": ")[0]: line.split(": ")[1].split(" ") for line in lines}

at = {("svr", False, False): 1}

total = 0
while len(at) > 0:
    working, seen_dac, seen_fft = random.choice(list(at.keys()))
    times_seen = at[(working, seen_dac, seen_fft)]
    del at[(working, seen_dac, seen_fft)]

    if working == "out":
        if seen_dac and seen_fft:
            total += times_seen
        continue

    if working == "dac":
        seen_dac = True
    if working == "fft":
        seen_fft = True

    for connection in connections[working]:
        if (connection, seen_dac, seen_fft) in at:
            at[(connection, seen_dac, seen_fft)] += times_seen
        else:
            at[(connection, seen_dac, seen_fft)] = times_seen

print(total)

print(f"time taken: {(time.time() - benchmark_start):.{4}f}s")
