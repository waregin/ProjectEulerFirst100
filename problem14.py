# The following iterative sequence is defined for the set of positive integers:
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
# Which starting number, under one million, produces the longest chain?

from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

limit = 10000000
max_chain = 0
max_starting = 0

n_to_chain_length = {1: 1}

for n in range(2, limit):
    curr_num = n
    count = 0
    while not curr_num in n_to_chain_length:
        if curr_num % 2 == 0:
            curr_num = int(curr_num / 2)
        else:
            curr_num = (3 * curr_num) + 1
        count += 1
    count += n_to_chain_length[curr_num]
    n_to_chain_length[n] = count
    if count > max_chain:
        max_chain = count
        max_starting = n
    if n % 1000000 == 0:
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')} examined through {n}...")

print(f"The starting number {max_starting} has the longest chain: {max_chain}")
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
