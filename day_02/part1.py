import utils
import time

data = utils.fetch_input(day=2)
# data = utils.fetch_small(day=2)
# data = utils.fetch_test(day=2)
benchmark_start = time.time()

data = "".join(data.split("\n"))
ranges = data.split(",")

total = 0
for r in ranges:
    start, end = r.split("-")

    l = len(start) if len(start) % 2 == 0 else len(start) + 1

    pattern = 10 ** (l // 2 - 1)
    if len(start) % 2 == 0:
        pattern = int(start[: len(start) // 2])

    while int(str(pattern) * 2) < int(start):
        pattern += 1
    while int(str(pattern) * 2) <= int(end):
        total += int(str(pattern) * 2)
        pattern += 1

print(total)
print(f"time taken: {(time.time() - benchmark_start):.{4}f}s")
