#!/usr/bin/python3
"""
This module defines a function that prints first_name and last_name
"""

def say_my_name(first_name, last_name=""):
    """
    The function takes in two string variables as prints the content inside them
    Args: 
    first_name (str): contains the first name
    last_name (str): contains the last name
    """
    
    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")
    if type(last_name) not in [str]:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
