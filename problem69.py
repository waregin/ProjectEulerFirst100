# Find the value of n <= 1,000,000 for which n/phi(n) is a maximum.
from datetime import datetime

print(f"{datetime.now().strftime('%H:%M:%S.%f')}")

limit = 1000000

is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(limit**0.5 + 1)):
    if is_prime[i]:
        k = i * i
        while k <= limit:
            is_prime[k] = False
            k += i

maximum_n = 1
for n in range(2, limit + 1):
    if is_prime[n]:
        new_max = maximum_n * n
        if new_max > limit:
            break
        maximum_n = new_max

print(f"found maximum n to be {maximum_n}")
print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
