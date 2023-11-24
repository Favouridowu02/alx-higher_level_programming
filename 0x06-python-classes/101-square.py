#!/usr/bin/python3
""" This module contains a function that defines a square:"""


class Square:
    """ This class defines a Square

        Attributes:
            size: A Private instance attribute
        Methods:
            area
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size: size of square
            position: the tuple containing the position
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Description: The area method used for calculating the
                    square of the size

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

    @property
    def position(self):
        """ This is used to get the value of the position

        Return: the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ This is used to set the position

        Args:
            pos: the position
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ prints in stdout the square with the character #"""
        if self.size == 0:
            print()
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(self.size):
            print("{}".format(" " * self.position[0]), end="")
            print("{}".format("#" * self.size))

    def __str__(self):
        """ prints in stdout the square with the character #"""
        if self.size != 0 and self.position[1] > 0:
            print("" * self.position[1])
        for i in range(self.size):
            print("{}".format(" " * self.position[0]), end="")
            print("{}".format("#" * self.size), end="")
            if i != self.size - 1:
                print("")
        return ("")
