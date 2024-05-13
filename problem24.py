# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
from datetime import datetime
from itertools import permutations

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
limit = 1000000

perms = permutations(digits)
limit_item = list(perms)[limit - 1]
item = "".join(limit_item)

print(int(item))
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
