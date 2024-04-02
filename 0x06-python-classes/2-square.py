#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """This class defines the init method to initialize size"""
    def __init__(self, size=0):
        """the init method initializes size as private instance attribute"""
        if (size.__class__ != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
