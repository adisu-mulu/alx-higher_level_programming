#!/usr/bin/python3
"""This module defines a class Square"""
class Square:
    """This class defines the init method to initialize size"""
    def __init__(self, size=0):
        """the init method initializes size as private instance attribute"""
        self.__size = size


    def size(self):
        return (self.__size)
    
    def size(self, value):
        if (value.__class__ != int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
        
    def area(self):
        return(self.__size **2)
