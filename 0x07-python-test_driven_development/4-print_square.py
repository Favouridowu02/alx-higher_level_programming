#!/usr/bin/python3
"""
    This module contains a function that prints a square with the character #
"""


def print_square(size):
    """
    This function print a square with the character #
    
    Arguments:
        size: the size length of the square

    Return: None
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size is float and size < 0:
        raise TypeError("size must be an integer")
    
    for i in range(int(size)):
        print("#" * size, end="\n")
