# How many, not necessarily distinct, values of (n r) for 1 <= n <= 100, are greater than one-million?
from datetime import datetime


def find_factorial(x):
    result = 1
    for i in range(x, 0, -1):
        result *= i
    return result


print(f"{datetime.now().strftime('%H:%M:%S.%f')}")

count = 0
for n in range(1, 101):
    for r in range(1, n + 1):
        # calculate (n r)
        fact_n = find_factorial(n)
        fact_r = find_factorial(r)
        fact_n_r = find_factorial(n - r)
        combinations = fact_n / (fact_r * fact_n_r)
        # if > 1000000, increase count
        if combinations > 1000000:
            count += 1

print(count)
print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
