# How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
from datetime import datetime
from math import factorial

print(f"{datetime.now().strftime('%H:%M:%S.%f')}")

n_to_next_n = {}


def find_next_n(n):
    if n in n_to_next_n.keys():
        return n_to_next_n[n]
    arr_n = [*str(n)]
    next = sum([factorial(int(d)) for d in arr_n])
    n_to_next_n[n] = next
    return next


limit = 1000000
num_sixty = 0

for n in range(1, limit):
    # calculate length of chain
    chain = [n]
    next_n = find_next_n(n)
    while next_n not in chain:
        chain.append(next_n)
        next_n = find_next_n(next_n)
    if len(chain) == 60:
        num_sixty += 1

print(
    f"{datetime.now().strftime('%H:%M:%S.%f')} found {num_sixty} chains with 60 unique terms"
)
