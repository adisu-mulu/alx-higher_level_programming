#!/usr/bin/python3
"""
This module defines a function that adds two integers
"""

def add_integer(a, b=98):

    """"
    The add_integer function takes one arguement and one positional arguement and returns the result of addition
    """
    if type(a) not in [int, float, None]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float, None]:
        raise TypeError("b must be an integer")
    if type(a) == None:
        raise TypeError("a must be an integer")
    if type(b) == None:
        raise TypeError("b must be an integer")
    if type(a) in [float]:
        a = int(a)
    if type(b) in [float]:
        b = int(b)
    return a+b
