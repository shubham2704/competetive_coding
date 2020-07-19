import sys
import math

e = input()

left = ''
right = ''

for i, char in enumerate(e):
    if i % 2 == 0:
        left += char
    else:
        right += char

print(bytes.fromhex(left + right).decode("ASCII"))
