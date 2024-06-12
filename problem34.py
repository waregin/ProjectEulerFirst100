# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
from datetime import datetime
import math


def is_digit_factorial(n):
    sum = 0
    for d in [*str(n)]:
        sum += math.factorial(int(d))
        if sum > n:
            return False
    return n == sum


print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
limit = 10000000
total = 0

for n in range(10, limit):
    if is_digit_factorial(n):
        total += n

print(total)
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
