#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for x in matrix:
            count = 0
            for y in x:
                print("{:d}".format(y), end='')
                count += 1
                if count != len(x):
                    print(" ", end='')
            print()
