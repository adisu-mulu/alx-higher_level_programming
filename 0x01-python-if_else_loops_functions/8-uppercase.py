#!/usr/bin/python3
def uppercase(str):
    strs = ""
    for letter in (str):
        digit = ord(letter)
        if digit in range(97, 123):
            digit = digit - 32
            upperCase = chr(digit)
        else:
            upperCase = letter
        strs = strs + upperCase
    print("{}".format(strs))
