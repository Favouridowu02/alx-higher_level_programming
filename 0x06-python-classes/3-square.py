#!/usr/bin/python3
""" This module contains a function that defines a square:"""


class Square:
    """ This class defines a Square

        Attributes:
            size: A Private instance attribute
        Methods:
            area
    """
    def __init__(self, size=0):
        """
        Args:
            size: size of square
        """

        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        Description: iThe area method used for calculating the square
                    of the size

        Return: square area
        """

        return self.__size ** 2
