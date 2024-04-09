#!/usr/bin/python3

"""
this module defines a function called print_square that takes as an arguement an integer
"""


def print_square(size):

    """ The function print_square takes an integer size and prints # for the squared amount of size
    Args: size (int): the initial size
"""
    
    if type(size) not in [int]:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) in [float] and size < 0:
        raise TypeError("size must be an integer")

    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()
