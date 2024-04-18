# Find the maximum total from top to bottom of the triangle
from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

# larger triangle
rows = []
rows.append([75])
rows.append([95, 64])
rows.append([17, 47, 82])
rows.append([18, 35, 87, 10])
rows.append([20, 4, 82, 47, 65])
rows.append([19, 1, 23, 75, 3, 34])
rows.append([88, 2, 77, 73, 7, 63, 67])
rows.append([99, 65, 4, 28, 6, 16, 70, 92])
rows.append([41, 41, 26, 56, 83, 40, 80, 70, 33])
rows.append([41, 48, 72, 33, 47, 32, 37, 16, 94, 29])
rows.append([53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14])
rows.append([70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57])
rows.append([91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48])
rows.append([63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31])
rows.append([4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23])

# smaller example, answer is 23
# rows = []
# rows.append([3])
# rows.append([7, 4])
# rows.append([2, 4, 6])
# rows.append([8, 5, 9, 3])

maximum_total = rows[0][0]
previous_index = 0
for i in range(1, len(rows) - 1):
    row = rows[i]
    next_row = rows[i + 1]

    max_first_sum = max(
        row[previous_index] + next_row[previous_index],
        row[previous_index] + next_row[previous_index + 1],
    )
    max_second_sum = max(
        row[previous_index + 1] + next_row[previous_index + 1],
        row[previous_index + 1] + next_row[previous_index + 2],
    )

    if max_first_sum >= max_second_sum:
        maximum_total += row[previous_index]
    else:
        maximum_total += row[previous_index + 1]
        previous_index = previous_index + 1
last_row = rows[-1]
if last_row[previous_index] >= last_row[previous_index + 1]:
    maximum_total += last_row[previous_index]
else:
    maximum_total += last_row[previous_index + 1]

print(maximum_total)
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
