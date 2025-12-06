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

num_fresh = 0
for ingredient in ingredients.splitlines():
    for r in ranges:
        if int(ingredient) in r:
            num_fresh += 1
            break

print(num_fresh)


print(f"time taken: {(time.time() - benchmark_start):.{4}f}s")