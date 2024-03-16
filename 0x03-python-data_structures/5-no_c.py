#!/usr/bin/python3
def no_c(my_string):
    x = 0
    newstring = []
    for val in my_string:
        if val == 'c' or val == 'C':
            continue
        else:
            newstring.append(val)
    return ''.join(newstring)
