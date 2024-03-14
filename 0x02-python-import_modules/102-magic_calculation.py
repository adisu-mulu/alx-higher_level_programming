#!/usr/bin/python3
def magic_calculation(a, b):
    c = 0
    if a < b:
        c = add(a, b)
    else:
        c = sub(a, b)
    return c


def add(a, b):
    return (a + b)


def sub(a, b):
    return (a - b)
