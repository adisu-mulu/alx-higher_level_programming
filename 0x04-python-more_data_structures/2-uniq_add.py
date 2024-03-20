#!/usr/bin/python3
def uniq_add(my_list=[]):
    temp = list(set(my_list))
    x = 0
    for val in temp:
        x = x + val
    return (x)
