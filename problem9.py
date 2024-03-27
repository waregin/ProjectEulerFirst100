# A Pythagorean triplet is a set of three natural numbers, a < b < c for which a squared + b squared = c squared
# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

def is_pythagorean(a,  b, c):
    return a < b < c and (a*a) + (b*b) == (c*c)


for i in range(1, 9998):
    for j in range(2, 9999):
        k = 10000 - i - j
        if is_pythagorean(i, j, k):
            print(i*j*k)
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
            exit()
