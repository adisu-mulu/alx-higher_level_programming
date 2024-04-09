#!/usr/bin/python3
"""
This module defines a function that divides a given matrix by a given integer
"""


def matrix_divided(matrix, div):
    """
    This function computes a new matrix which contains the content of matrix divided by the integer div
    Args:
    matrix (int): The matrix containing the integers
    div (int): The integer to divide the elements in the matrix
    """
    if any(not isinstance(col, (int, float)) for row in matrix for col in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    cols= len(matrix[0][:])
    for row in matrix:
        if len(row) != cols:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    newmatrix = [row[:] for row in matrix]
    x = -1
    for row in matrix:
        x = x + 1
        y = -1
        for col in row:
            y = y+ 1
            newmatrix[x][y] = round((col / div), 2)

    return newmatrix
