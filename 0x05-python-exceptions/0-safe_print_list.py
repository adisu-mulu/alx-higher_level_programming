#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    try:
        for i in range(x):
            print(i, end="")
            n = n+1
        print("\n")
        return (n)
    except IndexError:
        print("\n")
        return (n)
    
    
