import utils
import time

data = utils.fetch_input(day=1)
# data = utils.fetch_small(day=1)
# data = utils.fetch_test(day=1)
benchmark_start = time.time()

lines = data.splitlines()

num_zeros = 0
state = 50

for line in lines:
    if line[0] == "R":
        state += int(line[1:])
    else:
        state -= int(line[1:])

    state = state % 100

    if state == 0:
        num_zeros += 1

print(num_zeros)
print(f"time taken: {(time.time() - benchmark_start):.{4}f}s")
