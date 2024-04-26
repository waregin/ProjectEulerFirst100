# Find the sum of the digits in the number 100!.
from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

limit = 100
product = 1
for n in range(limit, 0, -1):
    product = product * n

print(product)

sum = 0
str_product = str(product)
for s in [*str_product]:
    sum += int(s)

print(sum)
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
