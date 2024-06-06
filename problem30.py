# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
from datetime import datetime


def is_sum_of_powers(n, p):
    digits = [*str(n)]
    sum = 0
    for d in digits:
        sum += int(d) ** p
    return sum == n


print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
limit = 1000000
power = 5
numbers = []

for n in range(10, limit):
    if is_sum_of_powers(n, power):
        numbers.append(n)

print(sum(numbers))
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
