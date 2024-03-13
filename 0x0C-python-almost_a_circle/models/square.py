#!/usr/bin/python3
"""
    This is the Square Class that inherits from Rectangle Class
"""
from rectangle import Rectangle


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

    def __str__(self):
        """
            This is the string Representation of Class
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)
