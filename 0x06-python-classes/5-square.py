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
        self.size = size

    def area(self):
        """
        Description: iThe area method used for calculating the square
                    of the size

        Return: square area
        """

        return self.__size ** 2

    @property
    def size(self):
        """ This is used to get the value of the size of the square

        Return: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """ This is used to set the value of the size of the square

        Args:
            size: the new value to set the size of the square to
        """
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        """ prints in stdout the square with the character #"""
        if self.size == 0:
            print()
            return
        for i in range(self.size):
            print("{}".format("#" * self.size))
