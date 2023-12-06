#!/usr/bin/python3
"""
    This module contains a function called add_integer for adding numbers
"""
def add_integer(a, b=98):
    """ A function that adds 2 integers together.

    Arguments:
        a: the first number to be added
        b: the second number to be added with a default value of 98

    Return: the sum of the two numbers (a and b)
    """

    try:
        if type(b) is str:
            raise TypeError("b must be an integer")
        if type(b) is float or int:
            b = int(b)
    except TypeError:
        raise TypeError("b must be an integer")
    try:
        if type(a) is float or int:
            a = int(a)
    except TypeError:
        raise TypeError("a must be an integer")

    return a + b
