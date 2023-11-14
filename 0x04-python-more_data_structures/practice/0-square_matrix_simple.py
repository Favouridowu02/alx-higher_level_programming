#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """a function that computes the square value of all integers of a matrix.
    Arguments:
        matrix: a 2 dimensional array

    Return: a squared version of matrix
    """
   square = [list(map(lambda x: x ** 2, i)) for i in matrix]
   return square
