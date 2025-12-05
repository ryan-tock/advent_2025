import utils
import time

benchmark_start = time.time()
data = open("input.txt", 'r').read()
# data = open("small.txt", 'r').read()
# data = open("test.txt", 'r').read()

ranges_text = data.split("\n\n")[0]
ingredients = data.split("\n\n")[1]

def parse_range(existing_ranges, start, end):
    if end <= start:
        return
    for r in existing_ranges:
        if start in r:
            parse_range(existing_ranges, r.stop, end)
            return
        if (end-1) in r:
            parse_range(existing_ranges, start, r.start)
            return
    existing_ranges.append(range(start, end))

ranges = []
for r in ranges_text.splitlines():
    first = r.split("-")[0]
    second = r.split("-")[1]

    ranges.append(range(int(first), int(second) + 1))

ranges.sort(key=lambda r: len(r), reverse=True)

trimmed_ranges = []
for r in ranges:
    parse_range(trimmed_ranges, r.start, r.stop)

total = 0
for r in trimmed_ranges:
    total += len(r)

print(total)


print(f"time taken: {(time.time() - benchmark_start):.{4}f}s")