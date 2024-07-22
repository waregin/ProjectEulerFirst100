# Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
from datetime import datetime


def find_digital_sum(num):
    digits = [int(d) for d in [*str(num)]]
    return sum(digits)


print(f"{datetime.now().strftime('%H:%M:%S.%f')}")

limit = 100
max_sum = 0

for a in range(limit):
    for b in range(limit):
        max_sum = max(max_sum, find_digital_sum(a**b))

print(max_sum)
print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
