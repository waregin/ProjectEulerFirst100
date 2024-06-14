# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
from datetime import datetime


def is_palindrome(s):
    return s == s[::-1]


print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
limit = 1000000
# palindromes = []
sum = 0

for n in range(1, limit):
    if is_palindrome(str(n)) and is_palindrome(str(bin(n)).removeprefix("0b")):
        # palindromes.append(n)
        sum += n

# print(palindromes)
# print(sum(palindromes))
print(sum)
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
