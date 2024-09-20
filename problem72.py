# How many elements would be contained in the set of reduced proper fractions for d <= 1,000,000?
from datetime import datetime

print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
limit = 1000000

factors = {}
is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int((limit / 2) + 1)):
    if is_prime[i]:
        k = i * 2
        while k <= limit:
            factors.setdefault(k, [])
            factors[k].append(i)
            is_prime[k] = False
            k += i

print(f"{datetime.now().strftime('%H:%M:%S.%f')} found all the factors")

sum = 0
for d in range(2, limit + 1):
    phi = d - 1
    if not is_prime[d]:
        # phi(n) = n * (1 - (1/f1)) * (1 - (1/f2)) ... where f1, f2... are unique factors of n
        phi = d
        for f in factors[d]:
            top = f - 1
            bottom = f
            num = phi * top
            num = num / bottom
            phi = num
    sum += phi

print(f"found {sum} elements in set")
print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
