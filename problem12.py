# What is the value of the first triangle number to have over five hundred divisors?
from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

def is_factor(possible_factor, num):
    return num % possible_factor == 0


def count_factors(num):
    count = 0
    for n in range(1, int(num**0.5) + 1):
        if is_factor(n, num):
            if num**0.5 == n:
                count += 1
            else:
                count += 2
    return count


triangle_num = 1
i = 1
while True:
    factor_count = count_factors(triangle_num)
    if factor_count > 1000:
        print(f"{triangle_num} is the {i}th triangle number and has {factor_count} factors")
        break
    i += 1
    triangle_num += i
    if i % 10000 == 0:
        print(f"checking {i}th triangle number")

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
