# Find the sum of all the primes below two million.
# 142913828922
from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

limit = 2000000
crosslimit = limit**0.5
sieve = [False for i in range(limit)]
sieve[0] = True
sieve[1] = True

for n in range(4, limit, 2):
    sieve[n] = True

for n in range(3, limit, 2):
    if not sieve[n]:
        for m in range(n*n, limit, 2*n):
            sieve[m] = True

sum = 0
for index, value in enumerate(sieve):
    if not value:
        sum += index

print(sum)
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
