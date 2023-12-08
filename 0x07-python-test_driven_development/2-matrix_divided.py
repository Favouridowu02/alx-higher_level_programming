#!/usr/bin/python3
def matrix_divided(matrix, divi):
    """ a function that divides all elements of a matrix

    Arguments:
        matr ix: the array to be divided
        div: the divisor
        
    Return: the value of the divided matrix
    """

    for i in matrix:
        for j in i:
            if type(i) is not int or float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(i) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size div")
        
    type(div) is not int or float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    list_t = list([lambda(x, i: round(i * 2) for i in x)], for x in matrix)
    
