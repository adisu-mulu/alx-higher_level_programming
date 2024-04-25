#!/usr/bin/python3
""" This module defines the base class for the project"""


class Base:
    """Defining the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializing the base class with a default id
           Arguements:
           id (int): integer id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
