# How many Lychrel numbers are there below ten-thousand?
from datetime import datetime


def reverse(num):
    digits = [*str(num)]
    digits.reverse()
    return int("".join(digits))


def is_palindrome(num):
    return num == reverse(num)


print(f"{datetime.now().strftime('%H:%M:%S.%f')}")

limit = 10001
count = 0

for n in range(1, limit):
    new_num = n + reverse(n)
    iterations = 0
    while not is_palindrome(new_num) and iterations <= 50:
        new_num = new_num + reverse(new_num)
        iterations += 1
    if not is_palindrome(new_num):
        count += 1

print(count)
print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
