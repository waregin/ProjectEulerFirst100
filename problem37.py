# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
primes = []
truncatable_primes = []


def is_factor(possible_factor, num):
    return num % possible_factor == 0


def is_prime(possible_prime):
    for i in primes:
        if i > possible_prime**0.5:
            break
        if is_factor(i, possible_prime):
            return False
    primes.append(possible_prime)
    return True


def is_truncatable(prime):
    strp = str(prime)
    if len(strp) <= 1:
        return False

    arrp_left = [*strp]
    arrp_right = [*strp]
    for i in range(len(strp) - 1):
        arrp_left.pop(0)
        arrp_right.pop()
        if (
            not int("".join(arrp_left)) in primes
            or not int("".join(arrp_right)) in primes
        ):
            return False
    return True


limit = 1000000
for n in range(2, limit):
    if is_prime(n) and is_truncatable(n):
        truncatable_primes.append(n)

print(truncatable_primes)
print(sum(truncatable_primes))
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
