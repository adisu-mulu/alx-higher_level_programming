#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)
    while len(a) < 2:
        a.append(0)
    while len(b) < 2:
        b.append(0)
    while len(a) > 2:
        a.remove[-1]
    while len(b) > 2:
        b.remove[-1]

    new_tuple = [a[0] + b[0], a[1] + b[1]]
    return tuple(new_tuple)
