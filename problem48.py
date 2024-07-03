# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

sum = 0

for n in range(1, 1001):
    sum += n**n

print(sum)
print(str(sum)[-10:])
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
