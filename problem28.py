# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

limit = 1001
biggest_val = limit**2

value = 1
add_val = 2
sum = value

while value < biggest_val:
    sum += add_val * 10
    sum += value * 4
    value += add_val * 4
    add_val += 2

print(sum)
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
