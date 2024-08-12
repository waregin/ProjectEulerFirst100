# Exactly four continued fractions, for N <= 13, have an odd period.
# How many continued fractions for N <= 10000 have an odd period?
from datetime import datetime
import decimal

context = decimal.Context(prec=1000)

print(f"{datetime.now().strftime('%H:%M:%S.%f')}")

limit = 10000
count = 0
# starting with n = 2, go through n = limit
for n in range(2, limit + 1):
    # calculate continued fraction period
    period = []
    root = context.sqrt(decimal.Decimal(n))
    a0 = int(root)
    if a0 == root:
        continue
    a = context.divide(1, context.subtract(root, a0))
    while True:
        a_n = int(a)
        period.append(a_n)
        if a_n == (2 * a0):
            break
        a = context.divide(1, context.subtract(a, a_n))

    # if period is of odd length, increment count
    if len(period) % 2 != 0:
        count += 1

print(count)
print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
