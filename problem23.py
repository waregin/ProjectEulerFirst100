# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

def findSumOfDivisors(num):
    sum = 1

    for f in range(2, int(num**0.5) + 1):
        if num % f == 0:
            sum += f
            if f != int(num / f):
                sum += int(num / f)

    return sum


limit = 28123

# first, find all abundant numbers
abundants = []
for n in range(12, limit + 1):
    if findSumOfDivisors(n) > n:
        abundants.append(n)
print(len(abundants))

# next, find all numbers < limit which are sums of abundant numbers
sumsOfAbundants = {}
for i in range(len(abundants)):
    for j in range(i, len(abundants)):
        a = abundants[i] + abundants[j]
        if a <= limit:
            sumsOfAbundants[a] = 0

print(len(sumsOfAbundants))

# then, add together all numbers not on the previous list
nonAbundantsSum = 0
for a in range(1, limit + 1):
    if not a in sumsOfAbundants:
        nonAbundantsSum += a

print(nonAbundantsSum)
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
