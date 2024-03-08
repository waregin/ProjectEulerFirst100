# Find the sum of all the multiples of 3 or 5 below 1000.

sum = 0

for n in range(3, 1000):
    if n % 3 == 0 or n % 5 == 0:
        sum += n

print(sum)
