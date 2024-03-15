# Find the largest palindrome made from the product of two 3-digit numbers.
# 906609

largest_palindrome = 0

for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        # check whether the product is a palindrome
        product = i * j
        list_product = [*str(product)]
        reversed_list = [*str(product)]
        reversed_list.reverse()
        if list_product == reversed_list:
            # if yes, check whether it is larger than our current largest palindrome
            if product > largest_palindrome:
                # if yes, set largest palindrome to product
                largest_palindrome = product
        
        # if product is smaller than our current largest, go to next i value
        if product < largest_palindrome:
            break

print(largest_palindrome)
