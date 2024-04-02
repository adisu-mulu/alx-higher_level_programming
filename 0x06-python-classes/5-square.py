#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """This class defines the init method to initialize size"""
    def __init__(self, size=0):
        """the init method initializes size as private instance attribute"""
        self.__size = size

    @property
    def size(self):
        """Thsi method retrieves the value of size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """This method sets the value of size
        Args:
             value: first param
        Returns: nothing

        """
        if (value.__class__ != int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """The method calculates the area of size"""
        return(self.__size ** 2)

    def my_print(self):
        """This function prints out # """
        val = self.size
        if (val == 0):
            print()
        else:
            for x in range(val):
                for y in range(val):
                    print("#", end="")
                print()
