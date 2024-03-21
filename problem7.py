# What is the 10001st prime number?
from datetime import datetime

prime_index = 100000
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
primes = [2]

def is_factor(possible_factor, num):
    return num % possible_factor == 0


def is_prime(possible_prime):
    if possible_prime in primes:
        return True
    for i in primes:
        if is_factor(i, possible_prime):
            return False
    primes.append(possible_prime)
    return True

n = 3
while True:
    is_prime(n)
    n += 2
    if len(primes) > prime_index:
        break

print(primes[prime_index])
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
