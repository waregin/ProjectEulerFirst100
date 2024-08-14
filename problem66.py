# x^2 - Dy^2 = 1        x^2 - 1 = Dy^2
# Find the value of D <= 1000 in minimal solutions of x for which the largest value of x is obtained.
from datetime import datetime
import decimal


def satifies_equation(x, y, d):
    return (x * x) - (d * y * y) == 1


context = decimal.Context(prec=1000)

print(f"{datetime.now().strftime('%H:%M:%S.%f')}")

limit = 1000
max_x = 0
d_max_x = 0
for d in range(2, limit + 1):
    # first, make sure d isn't a square
    root = context.sqrt(decimal.Decimal(d))
    if root % 1 == 0:
        continue
    # calculate continued fraction period
    a0 = int(root)
    period = []
    a = context.divide(1, context.subtract(root, a0))
    while True:
        a_n = int(a)
        period.append(a_n)
        if a_n == (2 * a0):
            break
        a = context.divide(1, context.subtract(a, a_n))

    index = 0
    x_n_2 = 0
    y_n_2 = 0
    x_n_1 = a0
    y_n_1 = 1
    x = (a0 * period[index]) + 1
    y = period[index]
    while not satifies_equation(x, y, d):
        # calculate convergent fraction with x as num and y as den
        index += 1
        if index == len(period):
            index = 0
        x_n_2 = x_n_1
        y_n_2 = y_n_1
        x_n_1 = x
        y_n_1 = y
        x = (x_n_1 * period[index]) + x_n_2
        y = (y_n_1 * period[index]) + y_n_2

    if x > max_x:
        max_x = int(x)
        d_max_x = d

print(f"found largest value of x to be {max_x} for D = {d_max_x}")
print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
