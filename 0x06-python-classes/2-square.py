#!/usr/bin/python3
""" This module contains a function that defines a square:"""


class Square:
    """ This class defines a Square

        Attributes:
            size: A Private instance attribute
        the pass statement is used
    """
    def __init__(self, size=0):
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")
