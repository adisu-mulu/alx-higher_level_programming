#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = []
    for var in my_list:
        if var == search:
            newlist.append(replace)
        else:
            newlist.append(var)
    return newlist
