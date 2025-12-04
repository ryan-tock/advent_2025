import utils
import time

benchmark_start = time.time()
data = open("input.txt", 'r').read()
# data = open("small.txt", 'r').read()
# data = open("test.txt", 'r').read()

lines = data.splitlines()
total = 0

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == '.':
            continue
        neighbors = [(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2)]
        neighbors = [n for n in neighbors if n != (x, y)]
        neighbors = [n for n in neighbors if n[0] >= 0 and n[1] >= 0]
        neighbors = [n for n in neighbors if n[1] < len(lines)]
        neighbors = [n for n in neighbors if n[0] < len(lines[n[1]])]

        count = 0
        for neighbor in neighbors:
            if lines[neighbor[1]][neighbor[0]] == '@':
                count += 1

        if count < 4:
            total += 1

print(total)


print(f"time taken: {(time.time() - benchmark_start):.{4}f}s")