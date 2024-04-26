#!/usr/bin/python3
""" This module defines the base class for the project"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """This method converts python objects to json strings"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return (json.dumps(list_dictionaries))
