#!/usr/bin/python3
"""
This module defines a class called Rectangle
"""


class Rectangle:
    """
    Class Rectangle implements the init function
    """
    def __init__(self, width=0, height=0):
        """ the init function initializes a new Rectangle object
        Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Returns the width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """sets the width of the rectangle
        Args:
        value (int): the new value
        """
        if not isinstance(value, int):
            raise TypeError("width mut be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """sets the height of the rectangle
        Args:
        value (int): the new value
        """
        if not isinstance(value, int):
            raise TypeError("height mut be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
