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

    found = set()

    for num_copies in range(2, len(end) + 1):
        pattern_length = (len(start) + num_copies - 1) // num_copies
        pattern = 10 ** (pattern_length - 1)
        if len(start) % num_copies == 0:
            pattern = int(start[:pattern_length])

        while int(str(pattern) * num_copies) < int(start):
            pattern += 1
        while int(str(pattern) * num_copies) <= int(end):
            found.add(int(str(pattern) * num_copies))
            pattern += 1

    total += sum(found)

print(total)
print(f"time taken: {(time.time() - benchmark_start):.{4}f}s")