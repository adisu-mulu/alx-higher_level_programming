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
            f"- {self.size}"
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
        self.__size = value

    def update(self, *args, **kwargs):
        """This function updates the attributes with args or
        kwargs if args is empty"""
        count = len(args)
        step = 0
        if len(args) > 0:
            if step < count:
                self.id = args[0]
                step += 1
            if step < count:
                self.size = args[1]
                step += 1
            if step < count:
                self.x = args[2]
                step += 1
            if step < count:
                self.y = args[3]
                step += 1
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
