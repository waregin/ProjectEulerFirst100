# How many n-digit positive integers exist which are also an nth power?
from datetime import datetime

print(f"{datetime.now().strftime('%H:%M:%S.%f')}")

count = 1
for x in range(2, 1001):
    for n in range(1, 1001):
        x_n = x**n
        length = len(str(x_n))
        if length == n:
            count += 1

print(count)
print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
