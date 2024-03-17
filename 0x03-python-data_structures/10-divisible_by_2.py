#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    x = 0
    newList = []
    while x < len(my_list):
        if my_list[x] % 2 == 0:
            newList.append(True)
            x += 1
        else:
            newList.append(False)
            x += 1
    return newList
