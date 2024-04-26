# Evaluate the sum of all the amicable numbers under 10000.
from datetime import datetime

def findSumOfDivisors(num):
    sum = 1

    for f in range(2, int(num**0.5) + 1):
        if num % f == 0:
            sum += f
            if f != int(num / f):
                sum += int(num / f)

    return sum


print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

limit = 10000

numToDivisorSum = {}
sumAmicables = 0

for n in range(2, limit):
    divisorSum = findSumOfDivisors(n)
    
    if numToDivisorSum.get(divisorSum, 0) == n:
        sumAmicables = sumAmicables + n + divisorSum
        print(f"Found set of amicables: {n} and {divisorSum}")
    
    numToDivisorSum[n] = divisorSum

print(sumAmicables)
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
