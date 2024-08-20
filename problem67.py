# Find the maximum total from top to bottom of the triangle
from datetime import datetime

print(f"{datetime.now().strftime('%H:%M:%S.%f')}")

# file triangle
rows = []
with open("0067_triangle.txt") as f:
    for line in f:
        # read in the line, splitting to list
        row = [int(n) for n in line.strip().split(" ")]
        rows.append(row)
    f.close()

# smaller example, answer 1074
# rows = []
# rows.append([75])
# rows.append([95, 64])
# rows.append([17, 47, 82])
# rows.append([18, 35, 87, 10])
# rows.append([20, 4, 82, 47, 65])
# rows.append([19, 1, 23, 75, 3, 34])
# rows.append([88, 2, 77, 73, 7, 63, 67])
# rows.append([99, 65, 4, 28, 6, 16, 70, 92])
# rows.append([41, 41, 26, 56, 83, 40, 80, 70, 33])
# rows.append([41, 48, 72, 33, 47, 32, 37, 16, 94, 29])
# rows.append([53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14])
# rows.append([70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57])
# rows.append([91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48])
# rows.append([63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31])
# rows.append([4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23])

sum_row = []
last_row = rows[-1]
for i in range(len(rows) - 2, -1, -1):
    sum_row = []
    second_last_row = rows[i]
    for j in range(len(second_last_row)):
        sum_row.append(
            max(second_last_row[j] + last_row[j], second_last_row[j] + last_row[j + 1])
        )
    last_row = sum_row

print(sum_row)
print(f"{datetime.now().strftime('%H:%M:%S.%f')}")
