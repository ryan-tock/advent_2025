import utils
import time

benchmark_start = time.time()
data = open("input.txt", 'r').read()
# data = open("small.txt", 'r').read()
# data = open("test.txt", 'r').read()

lines = data.splitlines()
max_len = max([len(l) for l in lines]) + 1
lines = [l + (max_len - len(l)) * ' ' for l in lines]
col_num = 0
working_op = '+'

total = 0
problem_val = 0
while col_num < len(lines[0]):
    if lines[-1][col_num] != ' ':
        working_op = lines[-1][col_num]
        problem_val = 1 if working_op == '*' else 0

    working_num = ''
    for row in range(len(lines)-1):
        working_num += lines[row][col_num]

    if working_num.strip() == '':
        total += problem_val
    else:
        if working_op == '+':
            problem_val += int(working_num.strip())
        else:
            problem_val *= int(working_num.strip())

    col_num += 1

print(total)
print(f"time taken: {(time.time() - benchmark_start):.{4}f}s")
