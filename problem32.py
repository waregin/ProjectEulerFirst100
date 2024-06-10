# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital
from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

products = {}

for i in range(2, 10000):
    for j in range(2, 1000):
        p = i * j
        digits = str(p) + str(i) + str(j)
        if len(digits) == 9:
            add = True
            for k in range(1, 10):
                if not str(k) in digits:
                    add = False
            if add:
                products[p] = 0

print(products)
print(sum(products.keys()))
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
