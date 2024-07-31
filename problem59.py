# The encryption key consists of three lower case characters.
# Using 0059_cipher.txt, a file containing the encrypted ASCII codes,
# and the knowledge that the plain text must contain common English words,
# decrypt the message and find the sum of the ASCII values in the original text.
from itertools import combinations
from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

# First, read in the file
f = open("0059_cipher.txt", "r")
cipher = [int(c) for c in f.read().split(",")]
f.close()

# Next, cycle through all combinations of lower case characters
alphabet = [*"abcdefghijklmnopqrstuvwxyz"]
possible_keys = list(combinations(alphabet * 3, 3))

# For each, convert to ASCII codes and perform XOR function to decrypt file
for key in possible_keys:
    key_codes = [ord(c) for c in key]

    key_index = 0
    decrypted_cipher = []
    for i in range(len(cipher)):
        xor = key_codes[key_index] ^ cipher[i]
        decrypted_cipher.append(xor)
        key_index += 1
        if key_index >= len(key_codes):
            key_index = 0

    # convert decrypted message back to characters
    decrypted_message = "".join([chr(c) for c in decrypted_cipher])

    # If decrypted message contains "the" or "The", print decrypted message
    if (
        "the" in decrypted_message
        and "and" in decrypted_message
        and "be" in decrypted_message
        and "to" in decrypted_message
        and "of" in decrypted_message
        and "that" in decrypted_message
    ):
        print(f"Used key of {key}")
        print(decrypted_message)
        break

# and sum up all ASCII values for decrypted message
print(sum(decrypted_cipher))
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
