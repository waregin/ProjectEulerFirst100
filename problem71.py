# By listing the set of reduced proper fractions for d <= 1,000,000 in ascending order of size,
# find the numerator of the fraction immediately to the left of 3 / 7.
from datetime import datetime

print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
limit = 1000000
target = 3 / 7

numerator = 2
denominator = 5
fraction = numerator / denominator
for d in range(2, limit + 1):
    start = int(d * fraction)
    for n in range(start, d):
        f = n / d
        if f >= target:
            break
        if f > fraction:
            numerator = n
            denominator = d
            fraction = f
            break

print(
    f"found fraction immediately left of 3/7 ({3/7}) to be {numerator}/{denominator} ({fraction})"
)
print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
