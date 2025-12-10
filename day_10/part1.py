import utils
import time
import heapq

data = utils.fetch_input(day=10)
# data = utils.fetch_small(day=10)
# data = utils.fetch_test(day=10)
benchmark_start = time.time()

lines = data.splitlines()


def get_indicator_code(indicator):
    val = 0
    p = 1
    for c in indicator:
        if c == 1:
            val += p
        p *= 2
    return val


total = 0
for line in lines:
    target = line.split(" ")[0]
    target = target[1:-1]
    target = [1 if n == "#" else 0 for n in target]

    buttons = line.split(" ")[1:-1]
    buttons = [n.split("(")[1].split(")")[0].split(",") for n in buttons]
    buttons = [[int(j) for j in n] for n in buttons]

    indicators = [0 for n in range(len(target))]

    state = (0, indicators)
    pqueue = []

    heapq.heappush(pqueue, state)
    seen = set()
    while len(pqueue) > 0:
        button_presses, indicators = heapq.heappop(pqueue)
        seen.add(get_indicator_code(indicators))

        if indicators == target:
            total += button_presses
            break

        for button in buttons:
            indicators_copy = indicators.copy()
            for indicator in button:
                indicators_copy[indicator] ^= 1

            indicator_code = get_indicator_code(indicators_copy)
            if indicator_code in seen:
                continue
            state = (button_presses + 1, indicators_copy)

            heapq.heappush(pqueue, state)

print(total)
print(f"time taken: {(time.time() - benchmark_start):.{4}f}s")
