import utils

data = open("input.txt", 'r').read()
# data = open("small.txt", 'r').read()
# data = open("test.txt", 'r').read()

ranges = data.split(',')

total = 0
for r in ranges:
    first = int(r.split('-')[0])
    second = int(r.split('-')[1])

    len1 = len(str(first))
    len2 = len(str(second))

    l = 0

    compare = 0

    if len1 % 2 == 0:
        l = len1
    else:
        l = len1 + 1

    compare = 10**(int(l/2) - 1)

    while int(str(compare) + str(compare)) < first:
        compare += 1

    while int(str(compare) + str(compare)) <= second:
        total += int(str(compare) + str(compare))
        compare += 1

print(total)