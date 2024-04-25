#!/usr/bin/python3
"""This modules defines the rectangle class"""


from models.base import Base


class Rectangle(Base):
    """ Class definition for the rectangle class inheriting base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialization of the rectangle class
        Arguements:
        width (int): width of th rectangle
        height (int): height of the rectangle
        x (int):
        y (int):
        """
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ Getter property for the width"""
        return self.__width

    @property
    def height(self):
        """getter property for the height"""
        return self.__height

    @property
    def x(self):
        """getter property for x"""
        return self.__x

    @property
    def y(self):
        """getter property for y"""
        return self.__y

    @width.setter
    def width(self, value):
        """setter property for width
        Arguements:
        value (int): the new value to be set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ setter property for height
    Arguement:
    value (int): the new value to be set for the height
    """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ setter property for x
        Arguement:
        value (int): the new value to be set for x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >0")
        self.__x = value

    @y.setter
    def y(self, value):
        """"setter property for y
        Arguement:
        value (int): the new value to be set for y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return (self.width * self.height)

    def display(self):
        """displays in # pattern the rectangle"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """modifies the string representation of the rectangle"""
        return (
                f"[Rectangle] ({self.id}) {self.x}/{self.y} "
                f"- {self.width}/{self.height}"
            )

    def update(self, *args, **kwargs):
        """This function updates the attriutes"""
        count = len(args)

        if count != 0:
            step = 0
            if step < count:
                self.id = args[0]
                step += 1
            if step < count:
                self.width = args[1]
                step += 1
            if step < count:
                self.height = args[2]
                step += 1
            if step < count:
                self.x = args[3]
                step += 1
            if step < count:
                self.y = args[4]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """This function return a dictionary representation of rectangle"""
        dict_rep ={
            'x':self._Rectangle__x,
            'y':self._Rectangle__y,
            'id': self.id,
            'height': self._Rectangle__height,
            'width': self._Rectangle__width
            }
        return dict_rep
