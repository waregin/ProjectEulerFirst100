# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

first = 1
second = 1
current = first + second
count = 3

while len(str(current)) < 1000:
    first = second
    second = current
    current = first + second
    count += 1

print(f"found {current} at index {count} to be the first 1000 digit Fibonacci number")
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
