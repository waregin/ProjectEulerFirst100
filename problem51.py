# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits)
# with the same digit, is part of an eight prime value family.
# 1. populate prime boolean array
# 2. for each prime, do all possible replacements (eg, for 56003, see the two 0s and replace them)
# and check how many are prime
# 3. when we get to a number meeting the conditions, stop and show the smallest prime
from datetime import datetime

print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
limit = 1000000
target = 8
is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(limit**0.5 + 1)):
    if is_prime[i]:
        k = i * i
        while k <= limit:
            is_prime[k] = False
            k += i

family = []
for i in range(limit):
    if is_prime[i]:
        # find the other numbers in the family
        str_i = str(i)
        num_primes = 0
        for digit in str_i:
            num_primes = 0
            family = []
            for d in range(10):
                new = int(str_i.replace(digit, str(d)))
                if new >= i:
                    family.append(new)
            # count how many are primes and break if match target
            for num in family:
                if is_prime[num]:
                    num_primes += 1
            if num_primes == target:
                break
        if num_primes == target:
            break

print(f"found family of {family} to have {target} primes")
print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
