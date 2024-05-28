# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
from datetime import datetime
import re
from decimal import Decimal, getcontext

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
getcontext().prec = 200000
pattern = re.compile(r"(.+?)\1+")
limit = 1000
max_length = 1
max_n = 1

for n in range(2, limit + 1):
    to_check = str(Decimal(1) / Decimal(n))
    found = re.findall(pattern, to_check)
    for cycle in found:
        length = len(cycle)
        if length > max_length:
            max_length = length
            max_n = n

print(f"1/{max_n} has a recurring cycle of {max_length} digits")
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
