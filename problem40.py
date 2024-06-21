# If d_n represents the nth digit of the fractional part, find the value of the following expression.
# d_1 x d_10 x d_100 x d_1000 x d_10000 x d_100000 x d_1000000
from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
limit = 1000000
fractional = "."
n = 1

while len(fractional) <= limit:
    fractional = fractional + str(n)
    n += 1

print(
    int(fractional[1])
    * int(fractional[10])
    * int(fractional[100])
    * int(fractional[1000])
    * int(fractional[10000])
    * int(fractional[100000])
    * int(fractional[1000000])
)
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
