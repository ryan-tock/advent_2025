import utils
import time

# data = utils.fetch_input(day=9)
data = utils.fetch_small(day=9)
# data = utils.fetch_test(day=9)
benchmark_start = time.time()

lines = data.splitlines()
red_tiles = [line.split(",") for line in lines]
red_tiles = [(int(line[0]), int(line[1])) for line in red_tiles]


def get_area(pair):
    return (abs(pair[0][0] - pair[1][0]) + 1) * (abs(pair[0][1] - pair[1][1]) + 1)


pairs = [
    (n, m) for i, n in enumerate(red_tiles) for j, m in enumerate(red_tiles) if j > i
]
pairs.sort(
    key=lambda x: get_area(x),
    reverse=True,
)
print(get_area(pairs[0]))

print(f"time taken: {(time.time() - benchmark_start):.{4}f}s")
