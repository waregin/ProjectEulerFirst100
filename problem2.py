# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
# 4613732

limit = 4000000

sum = 2
a = 3
b = 5
# 1, 2, 3, 5, 8, 13, 21, 34...

while b < limit:
    c = a + b
    sum += c
    a = b + c
    b = a + c

print(sum)
