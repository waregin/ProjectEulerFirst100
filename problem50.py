# Which prime, below one-million, can be written as the sum of the most consecutive primes?
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

max_consecutives = 0
sum_prime = 0
start = 0
while start < limit:
    num = 0
    sum = 0
    for i in range(start, limit):
        if is_prime[i]:
            sum += i
            num += 1
            if sum > limit:
                break
            if is_prime[sum] and num > max_consecutives:
                max_consecutives = num
                sum_prime = sum
    start += 1

print(f"found prime {sum_prime} to be the sum of {max_consecutives} primes")
print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
