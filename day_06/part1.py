import utils
import time

benchmark_start = time.time()
data = open("input.txt", 'r').read()
# data = open("small.txt", 'r').read()
# data = open("test.txt", 'r').read()

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
