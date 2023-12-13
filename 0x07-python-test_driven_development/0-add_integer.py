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

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
