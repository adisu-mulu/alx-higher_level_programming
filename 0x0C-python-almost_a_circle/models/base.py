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

    @classmethod
    def save_to_file(cls, list_objs):
        """ This method saves json rep of objects to file"""
        dataList = []
        if list_objs is None:
            with open(f"{cls.__name__}.json", 'w', encoding="utf-8") as f:
                f.write(dataList)
        else:
            for objs in list_objs:
                to_dict = objs.to_dictionary()
                dataList.append(to_dict)
            data = cls.to_json_string(dataList)
            with open(f"{cls.__name__}.json", 'w', encoding="utf-8") as f:
                f.write(data)
