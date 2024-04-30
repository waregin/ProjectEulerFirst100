# Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order.
# Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
# So, COLIN would obtain a score of 938 x 53 = 49714.
# What is the total of all the name scores in the file?
from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

f = open("0022_names.txt", "r")
names = f.read().split(",")
f.close()

names.sort()

total = 0
position = 1

for name in names:
    name = name.strip('"')
    score = 0
    for letter in [*name]:
        score += alphabet.index(letter)
    total += score * position
    position += 1

print(total)
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
