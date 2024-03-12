#!/usr/bin/python3
def pow(a, b):
    i = 0
    while (i < b):
        a = a * a
        i += 1
    if b < 0:
        return 1 / a
    if a < 0:
        return -1 * a
    if a < 0 and b < 0:
        return -1 / (-1 * a)
    return a
