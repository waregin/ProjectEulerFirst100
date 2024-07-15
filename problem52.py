# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
from datetime import datetime

print(f"{datetime.now().strftime('%H:%M:%S.%f')}")

x = 0
while True:
    x += 1
    arr_x = [*str(x)]
    arr_x1 = [*str(x * 2)]
    arr_x2 = [*str(x * 3)]
    arr_x3 = [*str(x * 4)]
    arr_x4 = [*str(x * 5)]
    arr_x5 = [*str(x * 6)]
    arr_x.sort()
    arr_x1.sort()
    arr_x2.sort()
    arr_x3.sort()
    arr_x4.sort()
    arr_x5.sort()
    if arr_x == arr_x1 == arr_x2 == arr_x3 == arr_x4 == arr_x5:
        break

print(x)
print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
