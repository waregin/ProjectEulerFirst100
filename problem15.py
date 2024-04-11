# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20x20 grid?
from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

limit = 20

# nxn = 2(n-1xn)
# n-1xn = n-1xn-1 + n-2xn
# ...
# 4xn = 3xn + 4xn-1
# 3xn = 2xn + 3xn-1
# 2xn = 1xn + 2xn-1
# 1xn = n + 1

# 6x6 = 2(1 + n + 2x5 + 3x5 + 4x5 + 5x5)
# nxn = 2(1xn + 2xn-1 + 3xn-1 + ... + n-1xn-1)

# num_routes = {(2,2): 6, (2,3): 10, (3,3): 20}
num_routes = {}

def count_routes(x, y):
    if x == 0 or y == 0:
        return 0
    if x == 1:
        return y + 1
    if (x, y) in num_routes:
        return num_routes[(x, y)]
    if x == y:
        # print(f"looking for {x}x{y}")
        value = 2 * count_routes(x - 1, y)
        num_routes[(x, y)] = value
        return value
    value = count_routes(x - 1, y) + count_routes(x, y - 1)
    num_routes[(x, y)] = value
    return value


# print(num_routes)
print(count_routes(limit, limit))
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
