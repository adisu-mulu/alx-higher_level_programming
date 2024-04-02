#!/usr/bin/python3


"""This module defines a class Square"""


class Square:
    """This class defines the init method to initialize size"""

    def __init__(self, size=0):
        """the init method initializes size as private instance attribute
        Args:
            size (int): the size of square
        Attributes:
            __size (int): private variable that stores size
        """
        if size.__class__ != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the computes the square of the size"""
        return(self.__size * self.__size)
