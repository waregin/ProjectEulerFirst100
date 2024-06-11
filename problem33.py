# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

fractions = {}

for n in range(10, 100):
    for d in range(n + 1, 100):
        for i in range(1, 10):
            strn = str(n)
            strd = str(d)
            stri = str(i)
            if stri in strn and stri in strd:
                numerator = int(strn.removeprefix(stri))
                denominator = int(strd.removeprefix(stri))
                if len(str(numerator)) > 1:
                    numerator = int(strn.removesuffix(stri))
                if len(str(denominator)) > 1:
                    denominator = int(strn.removesuffix(stri))

                if denominator > 0 and n / d == numerator / denominator:
                    fractions[n] = d
                    break

print(fractions)

total_num = 1
total_den = 1
for n in fractions.keys():
    total_num = total_num * n
    total_den = total_den * fractions[n]

print(total_den / total_num)
print((total_num / total_den).as_integer_ratio())
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
