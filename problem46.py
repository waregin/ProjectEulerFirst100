# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
# 9 = 7 + 2 x 1^2
from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
limit = 10000
primes = []
is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, limit + 1):
    if is_prime[i]:
        primes.append(i)
        k = i * i
        while k <= limit:
            is_prime[k] = False
            k += i
    elif i % 2 != 0:
        passes_conjecture = False
        for p in primes:
            if p > i:
                break
            num = i - p
            if num % 2 == 0:
                num = num / 2
                num = num**0.5
                if num % 1 == 0:
                    passes_conjecture = True
                    break
        if not passes_conjecture:
            print(i)
            break

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
