import utils
import time
from matplotlib.path import Path

data = utils.fetch_input(day=9)
# data = utils.fetch_small(day=9)
# data = utils.fetch_test(day=9)
benchmark_start = time.time()

lines = data.splitlines()
red_tiles = [line.split(",") for line in lines]
red_tiles = [(int(line[0]), int(line[1])) for line in red_tiles]
path = Path(red_tiles)


def get_area(pair):
    return (abs(pair[0][0] - pair[1][0]) + 1) * (abs(pair[0][1] - pair[1][1]) + 1)


vertical_lines_x = [
    red_tiles[i][0]
    for i in range(-1, len(red_tiles) - 1)
    if red_tiles[i][0] == red_tiles[i + 1][0]
]
vertical_lines_x.sort()
horizontal_lines_y = [
    red_tiles[i][1]
    for i in range(-1, len(red_tiles) - 1)
    if red_tiles[i][1] == red_tiles[i + 1][1]
]
horizontal_lines_y.sort()

pairs = [
    (n, m) for i, n in enumerate(red_tiles) for j, m in enumerate(red_tiles) if j > i
]
pairs.sort(
    key=lambda x: get_area(x),
    reverse=True,
)

for pair in pairs:
    min_x = min(pair[0][0], pair[1][0])
    max_x = max(pair[0][0], pair[1][0])
    min_y = min(pair[0][1], pair[1][1])
    max_y = max(pair[0][1], pair[1][1])

    corners = [(min_x, min_y), (max_x, min_y), (max_x, max_y), (min_x, max_y)]
    boundary1 = [(min_x, n - 1) for n in horizontal_lines_y if min_y < n - 1 < max_y]
    boundary2 = [(min_x, n + 1) for n in horizontal_lines_y if min_y < n + 1 < max_y]
    boundary3 = [(max_x, n - 1) for n in horizontal_lines_y if min_y < n - 1 < max_y]
    boundary4 = [(max_x, n + 1) for n in horizontal_lines_y if min_y < n + 1 < max_y]
    boundary5 = [(n - 1, min_y) for n in vertical_lines_x if min_x < n - 1 < max_x]
    boundary6 = [(n + 1, min_y) for n in vertical_lines_x if min_x < n + 1 < max_x]
    boundary7 = [(n - 1, max_y) for n in vertical_lines_x if min_x < n - 1 < max_x]
    boundary8 = [(n + 1, max_y) for n in vertical_lines_x if min_x < n + 1 < max_x]

    boundary = (
        corners
        + boundary1
        + boundary2
        + boundary3
        + boundary4
        + boundary5
        + boundary6
        + boundary7
        + boundary8
    )

    if all(path.contains_points(boundary, radius=1e-6)):
        print(pair)
        print(get_area(pair))
        break

print(f"time taken: {(time.time() - benchmark_start):.{4}f}s")
