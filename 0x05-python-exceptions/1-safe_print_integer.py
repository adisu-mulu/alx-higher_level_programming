#!/usr/bin/python3

def safe_print_integer(value):
    try:
        if (value.__class__ == int):
            print("{:d}\n".format(value))
            return 1
    except Exception:
        return 0
