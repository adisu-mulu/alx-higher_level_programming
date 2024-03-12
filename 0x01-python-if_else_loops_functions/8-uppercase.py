#!/usr/bin/python3
def uppercase(str):
    for letter in (str):
        digit = ord(letter)
        if digit in range(97, 123):
            digit = digit - 32
            upperCase = chr(digit)
        else:
            upperCase = letter
        print("{}".format(upperCase), end="")
    print("\n")
