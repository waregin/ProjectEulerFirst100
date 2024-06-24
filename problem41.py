# What is the largest n-digit pandigital prime that exists?
from datetime import datetime

simple_pans = {
    1: set("1"),
    2: set("12"),
    3: set("123"),
    4: set("1234"),
    5: set("12345"),
    6: set("123456"),
    7: set("1234567"),
    8: set("12345678"),
    9: set("123456789"),
}


def is_factor(possible_factor, num):
    return num % possible_factor == 0


def is_prime(possible_prime):
    for i in range(3, int(possible_prime**0.5) + 2, 2):
        if is_factor(i, possible_prime):
            return False
    return True


def is_n_pandigital(possible_pandigital, n):
    set_p = set(str(possible_pandigital))
    return "0" not in set_p and set_p == simple_pans[n]


print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
largest = 0

for n in range(87654321, 2142, -2):
    if is_n_pandigital(n, len(str(n))) and is_prime(n):
        largest = n
        break

print(largest)
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
