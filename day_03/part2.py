import utils
import time

data = utils.fetch_input(3)
# data = utils.fetch_small(3)
# data = utils.fetch_test(3)
benchmark_start = time.time()

lines = data.splitlines()
total = 0

for bank in lines:
    remaining_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    working_jolts = ""
    digits_remaining = 12
    while True:
        digit = remaining_digits[-1]
        if digit not in bank:
            remaining_digits.pop(-1)
            continue

        i = bank.index(digit)
        if len(bank) - i >= digits_remaining:
            working_jolts += bank[i]
            bank = bank[i+1:]
            remaining_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            digits_remaining -= 1
        else:
            remaining_digits.pop(-1)

        if digits_remaining == 0:
            break

    total += int(working_jolts)

print(total)

print(f"time taken: {(time.time() - benchmark_start):.{4}f}s")