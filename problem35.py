# How many circular primes are there below one million?
from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
primes = []


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


limit = 1000000
for n in range(2, limit):
    is_prime(n)
print(f"found {len(primes)} under {limit}")

count = 0
for p in primes:
    is_circular = True
    strp = str(p)
    arrp = [*strp]
    for i in range(len(strp)):
        arrp.append(arrp.pop(0))
        if not int("".join(arrp)) in primes:
            is_circular = False
            break
    if is_circular:
        count += 1

print(count)
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
