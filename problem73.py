# How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d <= 12,000?
from datetime import datetime

print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
lower_bound = 1 / 3
upper_bound = 1 / 2
limit = 12000

num_fractions = 0
for d in range(2, limit + 1):
    is_relative_prime = [True] * (d)
    is_relative_prime[0] = False
    for i in range(2, int(d / 2) + 1):
        if is_relative_prime[i] and d % i == 0:
            is_relative_prime[i] = False
            k = i * 2
            while k < d:
                is_relative_prime[k] = False
                k += i

    start = int(d * lower_bound)
    end = int(d * upper_bound) + 1
    for n in range(start, end):
        fraction = n / d
        # test whether n/d is reduced and between 1/3 and 1/2
        if is_relative_prime[n] and lower_bound < fraction < upper_bound:
            num_fractions += 1

print(f"{datetime.now().strftime('%H:%M:%S.%f')} found {num_fractions} fractions")
