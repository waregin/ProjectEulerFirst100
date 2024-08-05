# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
from datetime import datetime

print(f"{datetime.now().strftime('%H:%M:%S.%f')}")

# First, find all primes < 1,000,000
limit = 1000000
sieve = [True] * (limit + 1)
sieve[0] = sieve[1] = False

for i in range(2, int(limit**0.5) + 1):
    if sieve[i]:
        k = i * i
        while k <= limit:
            sieve[k] = False
            k += i


def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0:
        return False
    if num < limit:
        return sieve[num]
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


# get list of primes, excluding 2 and 5
primes = [3]
for i in range(7, 10000):
    if sieve[i]:
        primes.append(i)


def is_concatenating(p1, p2):
    concat1 = str(p1) + str(p2)
    concat2 = str(p2) + str(p1)
    return is_prime(int(concat1)) and is_prime(int(concat2))


lowest_sum = limit * limit
lowest_set = []
for i1 in range(100):
    p1 = primes[i1]
    for i2 in range(i1 + 1, len(primes)):
        p2 = primes[i2]
        if is_concatenating(p1, p2):
            for i3 in range(i2 + 1, len(primes)):
                p3 = primes[i3]
                prime_sum = sum([p1, p2, p3])
                if prime_sum > lowest_sum:
                    break
                if is_concatenating(p1, p3) and is_concatenating(p2, p3):
                    for i4 in range(i3 + 1, len(primes)):
                        p4 = primes[i4]
                        prime_sum = sum([p1, p2, p3, p4])
                        if prime_sum > lowest_sum:
                            break
                        if (
                            is_concatenating(p1, p4)
                            and is_concatenating(p2, p4)
                            and is_concatenating(p3, p4)
                        ):
                            for i5 in range(i4 + 1, len(primes)):
                                p5 = primes[i5]
                                prime_set = [p1, p2, p3, p4, p5]
                                prime_sum = sum(prime_set)
                                if prime_sum > lowest_sum:
                                    break
                                if (
                                    is_concatenating(p1, p5)
                                    and is_concatenating(p2, p5)
                                    and is_concatenating(p3, p5)
                                    and is_concatenating(p4, p5)
                                ):
                                    lowest_sum = prime_sum
                                    lowest_set = prime_set
                                    break

print(f"found 5 concatenating primes {lowest_set} with sum {lowest_sum}")
print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
