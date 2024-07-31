# If one complete new layer is wrapped around the spiral above,
# a square spiral with side length 9 will be formed. If this process is continued,
# what is the side length of the square spiral for which the ratio of primes along both diagonals
# first falls below 10%?
from datetime import datetime


def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


print(f"{datetime.now().strftime('%H:%M:%S.%f')}")

value = 1
add_val = 0
num_diagonals = 1
num_primes = 0

while True:
    add_val += 2
    for i in range(4):
        value += add_val
        if is_prime(value):
            num_primes += 1

    num_diagonals += 4
    percentage_primes = (num_primes / num_diagonals) * 100
    if percentage_primes < 10:
        print(
            f"found {num_primes} primes out of {num_diagonals} diagonal numbers "
            + f"for a percentage of {percentage_primes}"
        )
        break

print(f"sides of length {add_val + 1}")
print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
