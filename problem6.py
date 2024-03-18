# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum = 0
sum_squares = 0

for n in range(1, 101):
    sum += n
    sum_squares += (n * n)

squared_sum = sum * sum

print(f"square of sums: {squared_sum}")
print(f"sum of squares: {sum_squares}")
print(squared_sum - sum_squares)
