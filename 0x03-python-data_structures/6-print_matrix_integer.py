#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """a function that prints a matrix of integers
    """
    if matrix is None:
        print()
    else:
        for i in matrix:
            i = matrix.index(i)
            for j in matrix[i]:
                print("{}".format(j), end="")
                if matrix[i].index(j) < len(matrix[i]):
                    print(" ", end="") 
            print()
