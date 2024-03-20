#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortedD = dict(sorted(a_dictionary.items()))
    for key, val in sortedD.items():
        print(key+":", val)
