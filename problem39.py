# For which value of p <= 1000 is the number of solutions maximised?
from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
limit = 1001
max_solutions = 1
max_sol_p = 0

for p in range(12, limit):
    solutions = 0
    for a in range(1, p):
        for b in range(a, p - a):
            c = (a**2 + b**2) ** 0.5
            if c % 1 == 0 and (a + b + c) == p:
                solutions += 1
    if solutions > max_solutions:
        max_solutions = solutions
        max_sol_p = p

print(f"found {max_sol_p} to have {max_solutions} solutions")
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
