import utils
import time

data = utils.fetch_input(4)
# data = utils.fetch_small(4)
# data = utils.fetch_test(4)
benchmark_start = time.time()

lines = data.splitlines()
total = 0

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == '.':
            continue
        neighbors = utils.get_neighbors((x, y), len(lines[y]), len(lines))

        count = 0
        for neighbor in neighbors:
            if lines[neighbor[1]][neighbor[0]] == '@':
                count += 1

        if count < 4:
            total += 1

print(total)


print(f"time taken: {(time.time() - benchmark_start):.{4}f}s")