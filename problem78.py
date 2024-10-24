# Find the least value of n for which p(n) is divisible by one million.
# p(n) = p(n-1) + p(n-2) - p(n-5) - p(n-7) + p(n-12) + p(n-15) - p(n-22) - ...
# sequence 1, 2, 5, 7, 12, 15, 22, ...
# comes from k(3k - 1)/2, k(3k + 1)/2 where k starts at 1
from datetime import datetime

print(f"{datetime.now().strftime('%H:%M:%S.%f')}")

subtract_sequence = []
for k in range(1, 1000001):
    first = k * (3*k - 1) / 2
    second = k * (3*k + 1) / 2
    subtract_sequence.append(int(first))
    subtract_sequence.append(int(second))

p_dict = {}

def calculate_p(n):
    if n < 0:
        return 0
    if n <= 1:
        return 1
    if n in p_dict.keys():
        return p_dict[n]
    sum = 0
    is_subract = False
    count = 0
    for x in subtract_sequence:
        if x > n:
            break
        sub_p = calculate_p(n - x)
        if is_subract:
            sum -= sub_p
        else:
            sum += sub_p
        count += 1
        if count % 2 == 0:
            is_subract = not is_subract
    p_dict[n] = sum
    return sum

n = 10
while True:
    p = calculate_p(n)
    if n % 100000 == 0:
        print(f"{datetime.now().strftime('%H:%M:%S.%f')} found p({n}) = {p}")
    if p % 1000000 == 0:
        print(f"{datetime.now().strftime('%H:%M:%S.%f')} found p({n}) = {p}")
        break
    n += 1

# print(calculate_p(10))
print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
