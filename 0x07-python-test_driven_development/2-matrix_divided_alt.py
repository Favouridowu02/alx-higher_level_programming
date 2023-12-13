#!/usr/bin/python3
def matrix_divided(matrix, div):
    """ a function that divides all elements of a matrix

    Arguments:
        matr ix: the array to be divided
        div: the divisor
        
    Return: the value of the divided matrix
    """

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for j in i:
            if type(j) is not [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(i) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size div")
        
    if type(div) is not [int, float]:
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")

    list_t = [[round(i / div, 2) for x in row] for row in matrix]

    return list_t
