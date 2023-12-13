#!/usr/bin/python3
"""
This module contains the function matrix_divided which divides the
matrix by div
"""


def matrix_divided(matrix, div):
    """
    a function that divides all elements of a matrix without
    making any edits to the list itself

    Arguments:
        matr:x
        ix: the array to be divided
        div: the divisor

    Return: the value of the divided matrix
    """

    # Error msg for type checking
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list:
        raise TypeError(msg)
    for row in matrix:
        if type(row) is not list:
            raise TypeError(msg)
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError(msg)
        if len(row) is not len(matrix[0]):
            txt = "Each row of the matrix must have the same siz"
            raise TypeError(txt)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")

    list_t = [[round((elem / div), 2) for elem in row] for row in matrix]
    return list_t
