import utils

data = open("input.txt", 'r').read()
# data = open("small.txt", 'r').read()
# data = open("test.txt", 'r').read()

lines = data.splitlines()

num_zeros = 0
state = 50

for line in lines:
    if line[0] == 'R':
        state += int(line[1:])
    else:
        state -= int(line[1:])

    state = state % 100

    if state == 0:
        num_zeros += 1
print(num_zeros)