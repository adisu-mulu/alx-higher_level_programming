#!/usr/bin/python3
"""This module defines a class Square"""


class Square:

    """This class defines the init method to initialize size"""
    def __init__(self, size=0, position=(0, 0)):
        """the init method initializes size as private instance attribute
        Args:
             size (int): size of the square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Thsi method retrieves the value of size"""
        return (self.__size)

    def position(self):
        """Thsi method retrieves the value of position"""
        return (self.__position)

    @size.setter
    def size(self, value):
        """This method sets the value of size
        Args:
             value (int): first param
        Returns: nothing

        """
        if (value.__class__ != int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def position(self, value):
        """This method sets the value of size
        Args:
             value (int): first param
        Returns: nothing

        """
        for x in value:
            if x < 0:
                raise TypeError("position must be a tuple of 2 integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 integers")

        self.__position = value

    def area(self):
        """The method calculates the area of size"""
        return(self.__size ** 2)

    def my_print(self):
        """This function prints out # """
        val = self.__size
        a, b = self.__position
        if (val == 0):
            print()
        else:
            for x in range(val):
                for i in range(a):
                    print(" ", end="")
                for y in range(val):
                    print("#", end="")
                print()
