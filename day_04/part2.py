import utils
import time

data = utils.fetch_input(day=4)
# data = utils.fetch_small(day=4)
# data = utils.fetch_test(day=4)
benchmark_start = time.time()

lines = data.splitlines()


def remove_rolls(lines):
    total = 0
    removed = []

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == ".":
                continue
            neighbors = utils.get_neighbors((x, y), len(lines[y]), len(lines))

            count = 0
            for neighbor in neighbors:
                if lines[neighbor[1]][neighbor[0]] == "@":
                    count += 1

            if count < 4:
                removed.append((x, y))
                total += 1

    for square in removed:
        line = list(lines[square[1]])
        line[square[0]] = "."
        lines[square[1]] = "".join(line)
    return total


total = 0
while True:
    removed = remove_rolls(lines)
    total += removed
    if removed == 0:
        break

print(total)


print(f"time taken: {(time.time() - benchmark_start):.{4}f}s")
