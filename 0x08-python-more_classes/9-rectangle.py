#!/usr/bin/python3
"""
This module defines a class called Rectangle
"""


class Rectangle:
    """
    Class Rectangle implements the init function
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ the init function initializes a new Rectangle object
        Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Returns the width of the rectangle"""
        return (self.__width)

    @property
    def height(self):
        """Returns the height of the rectangle"""
        return (self.__height)

    @width.setter
    def width(self, value):
        """sets the width of the rectangle
        Args:
        value (int): the new value
        """
        if type(value) not in [int]:
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
        self.__height = value
        if type(value) not in [int]:
            raise TypeError("height mut be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
         """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with width and height equal to size.

        Args:
            size (int): The width and height of the new Rectangle.
        """
        return (cls(size, size))

    def area(self):

        """ Returns the area of the rectangle"""

        return (self.__width * self.__height)

    def perimeter(self):
        """ Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):

        if self.__width == 0 or self.__height == 0:
            return ""
        pattern = ''
        for x in range(self.__height):
            for y in range(self.__width):
                pattern = pattern + str(self.print_symbol)
            if x < self.__height - 1:
                pattern = pattern + '\n'

        return pattern

    def __repr__(obj):
        name = type(obj).__name__
        return f"{name}({obj.__width}, {obj.__height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
