# <p>The number, $1406357289$, is a $0$ to $9$ pandigital number because it is made up of each of the digits $0$ to $9$ in some order, but it also has a rather interesting sub-string divisibility property.</p>
# <p>Let $d_1$ be the $1$<sup>st</sup> digit, $d_2$ be the $2$<sup>nd</sup> digit, and so on. In this way, we note the following:</p>
# <ul><li>$d_2d_3d_4=406$ is divisible by $2$</li>
# <li>$d_3d_4d_5=063$ is divisible by $3$</li>
# <li>$d_4d_5d_6=635$ is divisible by $5$</li>
# <li>$d_5d_6d_7=357$ is divisible by $7$</li>
# <li>$d_6d_7d_8=572$ is divisible by $11$</li>
# <li>$d_7d_8d_9=728$ is divisible by $13$</li>
# <li>$d_8d_9d_{10}=289$ is divisible by $17$</li>
# </ul><p>Find the sum of all $0$ to $9$ pandigital numbers with this property.</p>
from datetime import datetime
from itertools import permutations

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

# first, find all 10-digit pandigitals
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
pandigitals = ["".join(pandigital) for pandigital in list(permutations(digits))]

# then, go through each and save in a list if they have the divisibility
pandigitals_with_property = []
primes = [2, 3, 5, 7, 11, 13, 17]

for pandigital in pandigitals:
    has_property = True
    for i in range(1, 8):
        if int(pandigital[i : i + 3]) % primes[i - 1] != 0:
            has_property = False
            break
    if has_property:
        pandigitals_with_property.append(int(pandigital))

# finally, print the sum of that list
print(sum(pandigitals_with_property))
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
