#!/usr/bin/python3
from models.rectangle import Rectangle
"""
    This is the Square Class that inherits from Rectangle Class
"""


class Square(Rectangle):
    """
    Arg:
        size: The size of the square
        x: the x-axis co-ordinate
        y: the y-axis co-ordinate
        id: the id
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        This is the initialization of the square class

        Arg:
            size: The size of the square
            x: the x-axis co-ordinate
            y: the y-axis co-ordinate
            id: the id
        """
        super().__init__(self, size, size, x, y, id)

    @property
    def size(self):
        """
            This function returns the size of the house
        """
        return size (self.size)

    @size.setter
    def size(self, size):
        """
            This is the setter functon for the size
        """
        self.width = size
        self.height = size

    def __str__(self):
        """
            This is the string Representation of Class
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                self.width)
