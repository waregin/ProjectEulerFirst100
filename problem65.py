# Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
from datetime import datetime
import decimal

print(f"{datetime.now().strftime('%H:%M:%S.%f')}")

# calculate continued fraction period
limit = 100
period = [2, 1]
rem = 2
while len(period) < limit:
    period.append(rem)
    period.append(1)
    period.append(1)
    rem += 2

num = 1
den = period[limit - 1]
for i in range(limit - 2, 0, -1):
    # print(f"num / den = {num} / {den}")
    addVal = period[i] * den
    temp = num + addVal
    num = den
    den = temp

num = num + (period[0] * den)
context = decimal.Context(prec=100)
print(f"period = {period}")
print(f"{limit}th convergent = {num} / {den} = {context.divide(num, den)}")
print(f"sum of num = {sum([int(d) for d in [*str(num)]])}")
print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
