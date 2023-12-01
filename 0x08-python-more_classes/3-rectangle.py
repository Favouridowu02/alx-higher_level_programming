#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """Representation of a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.height = height
        self.width = width

    def __str__(self):
        """ print the rectangle with the character #
            printable string representation of the rectangle
        """
        if (self.height == 0 or self.width == 0):
            return 0
        i = 0
        while i < self.height:
            print("#" * self.width, end="")
            if i != self.height - 1:
                print("")
            i += 1
        return ""

    def __repr(self):
        """
        """
        print(Rectangle)

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the rectangle area"""
        return (self.width * self.height)

    def perimeter(self):
        """ returns the rectangle perimeter"""
        if (self.height == 0 or self.width == 0):
            return 0
        return (2 * self.width) + (2 * self.height)
