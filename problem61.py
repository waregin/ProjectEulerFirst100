# Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type:
# triangle, square, pentagonal, hexagonal, heptagonal, and octagonal,
# is represented by a different number in the set.


def find_all_fours(func):
    fours = []
    n = 1
    x = func(n)
    while x < 10000:
        n += 1
        x = func(n)
        if len(str(x)) == 4:
            fours.append(x)
    return fours


def find_cyclicly(first_2, last_2, x_nss):
    if first_2 == last_2 and len(x_nss) == 0:
        return True
    result = []
    for x_ns in x_nss:
        nums = [x for x in x_ns if x.startswith(last_2)]
        for num in nums:
            last_two = num[2:]
            new_x_nss = x_nss.copy()
            new_x_nss.pop(new_x_nss.index(x_ns))
            result = find_cyclicly(first_2, last_two, new_x_nss)
            if result:
                if type(result) is not list:
                    result = []
                result.append(num)
                break
        if result:
            break
    return result


from datetime import datetime
from polygonals import *

print(f"{datetime.now().strftime('%H:%M:%S.%f')}")

t_ns = [str(x) for x in find_all_fours(find_t_n)]
q_ns = [str(x) for x in find_all_fours(find_q_n)]
p_ns = [str(x) for x in find_all_fours(find_p_n)]
h_ns = [str(x) for x in find_all_fours(find_h_n)]
s_ns = [str(x) for x in find_all_fours(find_s_n)]
o_ns = [str(x) for x in find_all_fours(find_o_n)]

nums = []
is_found = False
for t in t_ns:
    first_two = t[:2]
    last_two = t[2:]
    nums = find_cyclicly(first_two, last_two, [q_ns, p_ns, h_ns, s_ns, o_ns])
    if len(nums) == 5:
        nums.append(t)
        break

print(f"found {nums} with sum {sum([int(n) for n in nums])}")
print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
