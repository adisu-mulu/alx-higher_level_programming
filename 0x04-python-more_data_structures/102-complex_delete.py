#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keyS = list(a_dictionary.keys())

    for valueDel in keyS:
        if value == a_dictionary.get(valueDel):
            del a_dictionary[valueDel]

    return (a_dictionary)
