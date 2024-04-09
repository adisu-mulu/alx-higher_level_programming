#!/usr/bin/python3
"""
This module defines a function called text_indentation that takes in a string as an parameter
"""

def text_indentation(text):
    """
    The function text_indentation takes a string and for every occurence of '.', ',' and '?' prints a new line
    Args:
    text (str): the text 
"""
    if type(text) not in [str]:
        raise TypeError("text must be a string")
    for char in text:
        print("{}".format(char), end="")
        if char in ['.','?',':']:
            print()
            print()
        
