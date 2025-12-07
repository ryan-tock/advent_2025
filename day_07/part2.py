import utils
import time

data = utils.fetch_input(day=7)
# data = utils.fetch_small(day=7)
# data = utils.fetch_test(day=7)
benchmark_start = time.time()

lines = data.splitlines()
grid = [[n[i] for i in range(len(n))] for n in lines]
start = lines[0].index("S")

total = 1
line = 0
beams = {(0, start): 1}

while line < len(grid):
    new_beams = {}
    for row, col in beams:
        if grid[row][col] == "^":
            num_splits = beams[(row, col)]
            total += num_splits
            new_beams[(row, col + 1)] = new_beams.get((row, col + 1), 0) + num_splits
            new_beams[(row, col - 1)] = new_beams.get((row, col - 1), 0) + num_splits
        else:
            new_beams[(row, col)] = new_beams.get((row, col), 0) + beams[(row, col)]

    beams = new_beams
    beams = {(row + 1, col): beams[(row, col)] for row, col in beams}

    line += 1

print(total)

print(f"time taken: {(time.time() - benchmark_start):.{4}f}s")
