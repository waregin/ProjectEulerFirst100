# In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
# each expansion x = (num + den + den) of x - 1 / (num + den) of x - 1
from datetime import datetime

print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
limit = 1001
count = 0

numerator = 3
denomenator = 2
for i in range(2, limit):
    new_den = numerator + denomenator
    new_num = new_den + denomenator
    numerator = new_num
    denomenator = new_den
    if len(str(numerator)) > len(str(denomenator)):
        count += 1

print(count)
print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
