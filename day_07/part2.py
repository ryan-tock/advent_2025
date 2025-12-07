import utils
import time
from collections import defaultdict

data = utils.fetch_input(day=7)
# data = utils.fetch_small(day=7)
# data = utils.fetch_test(day=7)
benchmark_start = time.time()

lines = data.splitlines()
grid = [[n[i] for i in range(len(n))] for n in lines]
start = lines[0].index("S")

total = 1
line = 0
beams = defaultdict(int)
beams[start] = 1

while line < len(grid):
    new_beams = defaultdict(int)
    for col in beams:
        if grid[line][col] == "^":
            total += beams[col]
            new_beams[col + 1] += beams[col]
            new_beams[col - 1] += beams[col]
        else:
            new_beams[col] += beams[col]

    beams = new_beams
    line += 1

print(total)

print(f"time taken: {(time.time() - benchmark_start):.{4}f}s")
