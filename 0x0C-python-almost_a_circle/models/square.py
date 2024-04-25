#!/usr/bin/python3
"""This module defines a class that inherits the Rectangle class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This class defines the Square class that inherits Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """This function initializes the Square object
        Arguements:
        size (int): defines the width and height
        x (int):
        y (int):
        id (int):
        """
        self.__size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """modifies the string representation of the rectangle"""
        return (
            f"[Square] ({self.id}) {self.x}/{self.y} "
            f"- {self.width}"
          )

    @property
    def size(self):
        """ This method returns the size property value"""
        return self.__size

    @size.setter
    def size(self, value):
        """This method sets the size property"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >0")
        self.__width = value
        self.__height = value
