# Find the value of n, 1 < n < 10^7,
# for which phi(n) is a permutation of n and the ratio n/phi(n) produces a minimum.
from datetime import datetime


def is_permutation(x, y):
    arr_x = [*str(x)]
    arr_y = [*str(y)]
    arr_x.sort()
    arr_y.sort()
    return arr_x == arr_y


print(f"{datetime.now().strftime('%H:%M:%S.%f')}")

limit = 10**7

is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(limit**0.5 + 1)):
    if is_prime[i]:
        k = i * i
        while k <= limit:
            is_prime[k] = False
            k += i

minimum_phi = 0
minimum_ratio = limit
minimum_n = 0
for n1 in range(2, int(limit / 2) + 1):
    if is_prime[n1]:
        for n2 in range(n1 + 1, limit + 1):
            if is_prime[n2]:
                n = n1 * n2
                if n >= limit:
                    break
                # calculate phi(n)
                phi = n - n1 - n2 + 1
                ratio = n / phi
                # check if ratio is less than saved ratio
                # check if phi(n) is permutation of n
                if ratio < minimum_ratio and is_permutation(n, phi):
                    minimum_phi = phi
                    minimum_ratio = ratio
                    minimum_n = n

print(
    f"found n of {minimum_n} to have phi of {minimum_phi} and ratio of {minimum_ratio}"
)
print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
