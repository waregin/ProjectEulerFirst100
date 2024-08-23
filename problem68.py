# Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings.
# What is the maximum 16-digit string for a "magic" 5-gon ring?
from datetime import datetime
from itertools import permutations

print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lines = list(permutations(numbers, 3))

next_lines = {}
for line in lines:
    next_lines.setdefault(line, [])
    if 10 in [line[1], line[2]]:
        continue
    for next_line in lines:
        if 10 in [next_line[1], next_line[2]]:
            continue
        if sum(line) != sum(next_line):
            continue
        if (
            line[2] == next_line[1]
            and line[0] not in next_line
            and line[1] not in next_line
        ):
            next_lines[line].append(next_line)

possibities = []
for line1 in next_lines:
    for line2 in next_lines[line1]:
        for line3 in next_lines[line2]:
            for line4 in next_lines[line3]:
                for line5 in next_lines[line4]:
                    if line1[1] != line5[2]:
                        continue
                    exts = {line1[0], line2[0], line3[0], line4[0], line5[0]}
                    ints1 = [line1[1], line2[1], line3[1], line4[1], line5[1]]
                    ints2 = [line1[2], line2[2], line3[2], line4[2], line5[2]]
                    ints1.sort()
                    ints2.sort()
                    if ints1 != ints2 or len(exts) != 5 or min(exts) != line1[0]:
                        continue
                    possible = True
                    for key in exts:
                        if key in ints1:
                            possible = False
                    if possible:
                        possibities.append([line1, line2, line3, line4, line5])

max_possibility = 0
for possibility in possibities:
    new_list = []
    for item in possibility:
        new_list += list(item)
    sum = int("".join([str(n) for n in new_list]))
    max_possibility = max(max_possibility, sum)

print(max_possibility)
print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
