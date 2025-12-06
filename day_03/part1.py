import utils
import time

data = utils.fetch_input(day=3)
# data = utils.fetch_small(day=3)
# data = utils.fetch_test(day=3)
benchmark_start = time.time()

lines = data.splitlines()
total = 0

for bank in lines:
    max_jolts = 0
    for i in range(len(bank)-1):
        for j in range(i+1, len(bank)):
            jolts = int(bank[i] + bank[j])
            if jolts > max_jolts:
                max_jolts = jolts

    total += max_jolts

print(total)

print(f"time taken: {(time.time() - benchmark_start):.{4}f}s")