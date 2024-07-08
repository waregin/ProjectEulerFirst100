# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
# (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
# but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?
from datetime import datetime

print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
limit = 10001
increase_by = 3330
is_prime = [True] * limit
is_prime[0] = is_prime[1] = False

for i in range(2, limit):
    if is_prime[i]:
        k = i * i
        while k < limit:
            is_prime[k] = False
            k += i

sequence = []
for n in range(1000, limit - (increase_by * 2)):
    if n == 1487:
        continue
    n1 = n + increase_by
    n2 = n1 + increase_by
    if is_prime[n] and is_prime[n1] and is_prime[n2]:
        arr_n = [*str(n)]
        arr_n1 = [*str(n1)]
        arr_n2 = [*str(n2)]
        arr_n.sort()
        arr_n1.sort()
        arr_n2.sort()
        if arr_n == arr_n1 == arr_n2:
            sequence = [str(n), str(n1), str(n2)]
            break

print(sequence)
print("".join(sequence))
print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
