# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 
# 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

number_words = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand"
}

def find_letters(n, place):
    letters = ""
    num = int(n / place)
    if num > 0:
        letters = number_words[num] + number_words[place]
        if n % place > 0:
            letters = letters + "and"
    n = n - (num * place)
    return (n, letters)


limit = 1000
letter_count = 0

for n in range(1, limit + 1):
    letters = ""
    if n < 100 and n in number_words:
        letters = number_words[n]
    else:
        (n, word) = find_letters(n, 1000)
        letters = letters + word

        (n, word) = find_letters(n, 100)
        letters = letters + word
        
        if n in number_words:
            letters = letters + number_words[n]
        else:
            tens = int(n / 10)
            if tens > 0:
                tens = tens * 10
                letters = letters + number_words[tens]
            n = n - tens
            letters = letters + number_words[n]
    letter_count += len(letters)

print(letter_count)
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
