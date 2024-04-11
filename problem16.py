# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?
from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

limit = 1000
number = 2**limit
str_number = [*str(number)]
digits = [int(num) for num in str_number]

print(sum(digits))
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
