import utils
import time

data = utils.fetch_input(day=5)
# data = utils.fetch_small(day=5)
# data = utils.fetch_test(day=5)
benchmark_start = time.time()

ranges_text = data.split("\n\n")[0]
ingredients = data.split("\n\n")[1]

ranges = []
for r in ranges_text.splitlines():
    first = r.split("-")[0]
    second = r.split("-")[1]

    ranges.append(range(int(first), int(second) + 1))

ranges.sort(key=lambda x: x.start)

i=1
while i < len(ranges):
    start = ranges[i].start
    end = ranges[i].stop
    if start < ranges[i-1].stop:
        if end-1 < ranges[i-1].stop:
            ranges.pop(i)
            i -= 1
        else:
            ranges[i] = range(ranges[i - 1].stop, end)
    i += 1

total = sum([len(n) for n in ranges])
print(total)

print(f"time taken: {(time.time() - benchmark_start):.{4}f}s")