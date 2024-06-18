# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ..., n) where n > 1
from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

concatenations = []

for i in range(1, 10000):
    concatenated = ""
    for j in range(1, 100):
        p = i * j
        concatenated = concatenated + str(p)
        if len(concatenated) == 9:
            add = True
            for k in range(1, 10):
                if not str(k) in concatenated:
                    add = False
                    break
            if add:
                concatenations.append(concatenated)
            break
        if len(concatenated) > 9:
            break

print(concatenations)
print(max(concatenations))
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
