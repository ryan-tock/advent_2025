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

    found = set()

    if len1 == len2:
        for i in range(1, (len1 // 2) + 1):
            if len1 % i == 0:
                f = len1 // i
                compare = str(first)[:i]
                while first > int(compare * f):
                    compare = str(int(compare) + 1)

                while int(compare * f) <= second:
                    if (compare * f) not in found:
                        total += int(compare * f)
                        found.add(compare * f)
                    compare = str(int(compare) + 1)

    else:
        for i in range(1, (len1 // 2) + 1):
            if len1 % i == 0:
                f = len1 // i
                compare = str(first)[:i]
                while first > int(compare * f):
                    compare = str(int(compare) + 1)

                while len(compare * f) == len1:
                    if (compare * f) not in found:
                        total += int(compare * f)
                        found.add(compare * f)
                    compare = str(int(compare) + 1)

        for i in range(1, (len2 // 2) + 1):
            if len2 % i == 0:
                f = len2 // i
                compare = str(int("1" + ("0" * (i - 1))))

                while int(compare * f) <= second:
                    if (compare * f) not in found:
                        total += int(compare * f)
                        found.add(compare * f)
                    compare = str(int(compare) + 1)

print(total)