# How many different ways can one hundred be written as a sum of at least two positive integers?
# f(n) = the number of ways n can be represented as the sum of at least two positive integers
# f(n, x) where x < n = the number of ways n can be represented as the sum of integers starting with x

# f(1) = 0
# f(2) = 1
# f(3) = 2
# f(n) = f(n, 1) + f(n, 2) + f(n, 3) + .... + f(n, n-1)
# f(n, 1) = 1
# f(n, 2) = floor(n / 2)
# f(n, x) = f(n-x, 1) + f(n-x, 2) + f(n-x, 3) + ... + f(n-x, x) where x < n/2
# f(n, x) = f(n-x) where n - x == x + 1
# f(n, x) = f(n-x) + 1 where x >= n/2
# f(n, n-1) = 1
from datetime import datetime

print(f"{datetime.now().strftime('%H:%M:%S.%f')}")


def count_sums(n):
    if n <= 3:
        return n - 1
    sum = 0
    for i in range(1, n):
        sum += count_sums_largest_x(n, i)
    return sum


def count_sums_largest_x(n, x):
    if x >= n:
        return 0
    if x == 1:
        return 1
    if x == 2:
        return int(n / 2)
    if x == n - 1:
        return 1
    if x + 1 == n - x:
        return count_sums(n - x)
    if x < n / 2:
        sum = 0
        for i in range(1, x + 1):
            sum += count_sums_largest_x(n - x, i)
        return sum
    return count_sums(n - x) + 1


print(count_sums(100))
print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
