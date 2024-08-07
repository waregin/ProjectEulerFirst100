# Find the smallest cube for which exactly five permutations of its digits are cube.
from datetime import datetime

print(f"{datetime.now().strftime('%H:%M:%S.%f')}")

cubes = {}
for x in range(10000):
    cube = x**3
    perm_array = [*str(cube)]
    perm_array.sort()
    smallest_perm = "".join(perm_array)
    data = (cube, 1)
    if smallest_perm in cubes:
        data = cubes[smallest_perm]
        data = (data[0], data[1] + 1)
    cubes[smallest_perm] = data

smallest_cube = 100000000000000
for data in cubes.values():
    if data[1] == 5 and data[0] < smallest_cube:
        smallest_cube = data[0]

print(smallest_cube)
print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
