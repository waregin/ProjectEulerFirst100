# What is the first value which can be written as the sum of primes in over five thousand different ways?

# f(n) = the number of ways n can be represented as the sum of at least two primes
# f(n, x) = the number of ways n can be represented as the sum of primes starting with x (x must be < n)

# f(n) = f(n, 2) + f(n, 3) + f(n, 5) + ... + f(n, y) where y is the largest prime smaller than n
# f(2) = 0
# f(3) = 0
# f(5) = 1

# f(n, 2) = 1 if n is even, 0 if n is odd
# f(n, 3) = f(n-3, 2) + f(n-3, 3)

# f(n, x) = f(n-x, 2) + f(n-x, 3) + f(n-x, 5) + ... + f(n-x, x) where n-x > x
# f(n, x) = f(n-x) + 1 where n-x <= x
from datetime import datetime

print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
limit = 100
target = 5000

is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(limit**0.5 + 1)):
    if is_prime[i]:
        k = i * i
        while k <= limit:
            is_prime[k] = False
            k += i
primes = [i for i in range(len(is_prime)) if is_prime[i]]

def count_sums(n):
    if n <= 3:
        return 0
    sum = 0
    for p in primes:
        if p >= n:
            break
        sum += count_sums_largest_x(n, p)
    return sum


def count_sums_largest_x(n, x):
    if x >= n:
        return 0
    if x == 2:
        return 1 if n % 2 == 0 else 0
    if x <= n-x:
        sum = 0
        for p in primes:
            if p > x:
                break
            sum += count_sums_largest_x(n - x, p)
        return sum
    return count_sums(n - x) + 1

n = 10
while n <= limit:
    count = count_sums(n)
    if count > target:
        print(f"found count of {count} for n of {n}")
        break
    if n % 10 == 0:
        print(f"counted sums through n = {n}")
    n += 1

print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
