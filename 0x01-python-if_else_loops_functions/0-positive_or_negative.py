#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number == 0:
    print("{} is zero".format(number))
if number > 0:
    print("{} is postivie".format(number))
if number < 0:
    print("{} is negative".format(number))
