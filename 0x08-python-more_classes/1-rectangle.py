#!/usr/bin/python3
""" an empty class Rectangle that defines a rectangle"""


class Rectangle:
    """An empty class called Rectangle"""

    def __init__(self, width=0, height=0):
        """ The initialization of the instance with properties

        Arguments:
            width: the width of the rectangles
            height: the height of the rectangles
        """

        self.width = width
        self.height = height

        @property
        def width(self):
            """ To retrieve the width """
            return self.__width

        @width.setter
        def width(self, value):
            """
            To set the value of the width

            Width must be an integer, otherwise raise a TypeError exception with
            the message width must be an integer
            if width is less than 0, raise a ValueError exception with the message
            width must be >= 0
            Arguments:
                value: the value to change width to
                """
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """ To retrieve the height """
            return self.__height

        @height.setter
        def height(self, value):
            """ To set the value of the height

            height must be an integer, otherwise raise a TypeError exception with
            the message height must be an integer
            if height is less than 0, raise a ValueError exception with the message
            height must be >= 0
            Arguments:
            value: the value to change height to
            """
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
