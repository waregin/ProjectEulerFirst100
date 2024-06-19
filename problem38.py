# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ..., n) where n > 1
from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

largest = 0

for i in range(1, 10000):
    concatenated = ""
    for j in range(1, 10):
        p = i * j
        concatenated = concatenated + str(p)
        if len(concatenated) == 9:
            is_pandigital = True
            for k in range(1, 10):
                if not str(k) in concatenated:
                    is_pandigital = False
                    break
            if is_pandigital:
                largest = max(int(concatenated), largest)
            break
        if len(concatenated) > 9:
            break

print(largest)
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
