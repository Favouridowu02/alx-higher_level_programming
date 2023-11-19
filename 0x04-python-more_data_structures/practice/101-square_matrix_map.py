#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    """a function that computes the square value of all integers of a
    matrix using map

    Arguments:
        matrix: the 2 dimensional array of numbers

    Return: a new matrix containing the squares of the elements
    """
    my_list = list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
    return my_list
