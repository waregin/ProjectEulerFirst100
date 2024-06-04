# Considering quadratics of the form n^2 + an + b, where |a| < 1000 and |b| <= 1000
# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n, starting with n = 0.
from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
primes = [2]
limit = 1000


def is_factor(possible_factor, num):
    return num % possible_factor == 0


def is_prime(possible_prime):
    if possible_prime < 2:
        return False
    if possible_prime in primes:
        return True
    for i in range(2, int(possible_prime**0.5) + 2):
        if is_factor(i, possible_prime):
            return False
    primes.append(possible_prime)
    return True


def find_answer(a, b, n):
    return (n * n) + (a * n) + b


max_num_primes = 0
max_a_b = (0, 0)

for a in range((limit - 1) * -1, limit):
    for b in range(2, limit + 1):
        if not is_prime(b):
            continue
        count = 0
        for n in range(limit * limit):
            if is_prime(find_answer(a, b, n)):
                count += 1
            else:
                break
        if count > max_num_primes:
            max_num_primes = count
            max_a_b = a, b

print(f"Found {max_num_primes} primes for a = {max_a_b[0]} and b = {max_a_b[1]}")
print(f"a * b = {max_a_b[0] * max_a_b[1]}")
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
