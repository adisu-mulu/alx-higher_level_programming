#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mydict = {}
    for key, value in a_dictionary.items():
        mydict.update({key: (value * 2)})
    return mydict
