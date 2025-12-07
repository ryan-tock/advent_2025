import utils
import time

data = utils.fetch_input(day=7)
# data = utils.fetch_small(day=7)
# data = utils.fetch_test(day=7)
benchmark_start = time.time()

lines = data.splitlines()
grid = [[n[i] for i in range(len(n))] for n in lines]
start = lines[0].index("S")

total = 0
line = 0
beams = {start}

while line < len(grid):
    new_beams = set()
    for col in beams:
        if grid[line][col] == "^":
            total += 1
            new_beams.add(col + 1)
            new_beams.add(col - 1)
        else:
            new_beams.add(col)

    beams = new_beams
    line += 1

print(total)

print(f"time taken: {(time.time() - benchmark_start):.{4}f}s")
