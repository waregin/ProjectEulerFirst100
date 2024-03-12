# What is the largest prime factor of the number 600851475143?
# 6857

primes = []


def is_factor(possible_factor, num):
    return num % possible_factor == 0


def is_prime(possible_prime):
    for i in primes:
        if is_factor(i, possible_prime):
            return False
    primes.append(possible_prime)
    return True


NUMBER = 600851475143

largest_prime = 0
for n in range(2, int(NUMBER**0.5)):
    if is_factor(n, NUMBER) and is_prime(n):
        largest_prime = n

print(largest_prime)
