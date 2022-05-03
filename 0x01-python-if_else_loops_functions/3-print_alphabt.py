#!/usr/bin/python3
import string
for letter in string.ascii_lowercase:
    if letter == 'e' or letter == 'q':
	continue
    else:
	print(letter, end="")
