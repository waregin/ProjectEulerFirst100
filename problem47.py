# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
from datetime import datetime

primes = [2]


def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    for p in primes:
        if p > x**0.5:
            break
        if x % p == 0:
            return False
    primes.append(x)
    return True


print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
target = 4
consecutives = []

n = 1
while len(consecutives) < target:
    n += 1
    if is_prime(n):
        consecutives = []
    else:
        checking = n
        factors = {}
        for p in primes:
            if p > checking:
                break
            while checking % p == 0:
                factors[p] = 0
                checking = checking / p
        if len(factors) == target:
            consecutives.append(n)
        else:
            consecutives = []

print(consecutives)
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
