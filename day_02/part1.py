import utils
import time

benchmark_start = time.time()
data = open("input.txt", 'r').read()
# data = open("small.txt", 'r').read()
# data = open("test.txt", 'r').read()

ranges = data.split(',')

total = 0
for r in ranges:
    start, end = r.split('-')

    l = len(start) if len(start) % 2 == 0 else len(start) + 1

    pattern = 10 ** (l // 2 - 1)
    if len(start) % 2 == 0:
        pattern = int(start[:len(start)//2])

    while int(str(pattern) * 2) < int(start):
        pattern += 1
    while int(str(pattern) * 2) <= int(end):
        total += int(str(pattern) * 2)
        pattern += 1

print(total)
print(f"time taken: {(time.time() - benchmark_start):.{4}f}s")