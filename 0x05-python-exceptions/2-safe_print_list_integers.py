#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    count = 0
    try:
        while (n < x):
            if(my_list[n].__class__ == int):
                print("{:d}".format(my_list[n]), end="")
                n += 1
                count += 1
            else:
                n += 1
        print()
        return (count)
    except Exception:
        pass
