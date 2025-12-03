import utils
import time

benchmark_start = time.time()
data = open("input.txt", 'r').read()
# data = open("small.txt", 'r').read()
# data = open("test.txt", 'r').read()

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