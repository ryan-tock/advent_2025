import utils
import time

data = utils.fetch_input(6)
# data = utils.fetch_small(6)
# data = utils.fetch_test(6)
benchmark_start = time.time()

lines = data.splitlines()
grid = [line.split() for line in lines]
cols = [[line[n] for line in grid] for n in range(len(grid[0]))]

def product(l):
    p = 1
    for n in l:
        p *= n
    return p

total = 0
for col in cols:
    op = col[-1]
    nums = [int(n) for n in col[:-1]]

    if op == '+':
        total += sum(nums)
    else:
        total += product(nums)

print(total)

print(f"time taken: {(time.time() - benchmark_start):.{4}f}s")
