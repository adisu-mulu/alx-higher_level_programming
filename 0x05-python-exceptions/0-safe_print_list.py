#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    while(n < x):
        try:
            print(my_list[n], end="")
            n = n+1
        except IndexError:
            break
    print("\n")
    return (n)
