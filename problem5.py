# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# 232792560

# 20 = 2 * 2 * 5
# 19 = 19
# 18 = 2 * 3 * 3
# 17 = 17
# 16 = 2 * 2 * 2 * 2
# 15 = 3 * 5
# 14 = 2 * 7
# 13 = 13
# 12 = 2 * 2 * 3
# 11 = 11
# 10 = 2 * 5
# 9 = 3 * 3
# 8 = 2 * 2 * 2
# 7 = 7
# 6 = 2 * 3
# 5 = 5
# 4 = 2 * 2
# 3 = 3
# 2 = 2

primes = []

def is_factor(possible_factor, num):
    return num % possible_factor == 0


def is_prime(possible_prime):
    if possible_prime in primes:
        return True
    for i in primes:
        if is_factor(i, possible_prime):
            return False
    primes.append(possible_prime)
    return True


num_primes = {}

# in range 2-20 inclusive
for n in range(2, 21):
    # find prime factors
    for i in range(2, n + 1):
        if is_factor(i, n) and is_prime(i):
            curr_num_primes = 0
            while is_factor(i, n):
                curr_num_primes += 1
                n = n / i
            # check dictionary for prime factors
            if num_primes.get(i, 0) < curr_num_primes:
                # if num of a prime factor < curr num of that, increase dict
                num_primes[i] = curr_num_primes

answer = 1
for key in num_primes:
    count = num_primes[key]
    for j in range(0, count):
        answer = answer * key

print(answer)
