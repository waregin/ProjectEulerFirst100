# Given that L is the length of the wire, for how many values of L <= 1,500,000
# can exactly one integer sided right angle triangle be formed?
from datetime import datetime

print(f"{datetime.now().strftime('%H:%M:%S.%f')}")

limit = 1500000
start = (3, 4, 5)
primitives = [start]

# find primitive Pythagorean triples
def find_next_triples(a, b, c):
    if a + b + c > limit:
        return
    a_one = a - 2*b + 2*c
    b_one = 2*a - b + 2*c
    c_one = 2*a - 2*b + 3*c
    a_two = a + 2*b + 2*c
    b_two = 2*a + b + 2*c
    c_two = 2*a + 2*b + 3*c
    a_three = -a + 2*b + 2*c
    b_three = -2*a + b + 2*c
    c_three = -2*a + 2*b + 3*c
    primitives.append((a_one, b_one, c_one))
    primitives.append((a_two, b_two, c_two))
    primitives.append((a_three, b_three, c_three))
    find_next_triples(a_one, b_one, c_one)
    find_next_triples(a_two, b_two, c_two)
    find_next_triples(a_three, b_three, c_three)

find_next_triples(*start)

# for each primitive, find the perimeter
perimeter_to_count = {}
for primitive in primitives:
    p = sum(primitive)
    new_p = p
    # multiply the perimeter until limit is exceeded, counting along the way
    while new_p <= limit:
        perimeter_to_count.setdefault(new_p, 0)
        perimeter_to_count[new_p] += 1
        new_p += p

# go through perimeter dictionary, find all perimeters with 1 triple
print(sum([1 for p in perimeter_to_count if perimeter_to_count[p] == 1]))
print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
