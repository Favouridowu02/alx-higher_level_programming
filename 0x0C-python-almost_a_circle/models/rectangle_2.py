#!/usr/bin/python3
"""
    This module contains a Class called Rectangle that inherits
    from Base module
"""
from models.base import Base


class Rectangle(Base):
    """
        This Class inherits from the Base Class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            This is the initialization of the Rectangle Class
            
            Arguments:
                Width: the width
                Height: The height
                x: the x
                y: the y

            Return: None
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ This is the getter function for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """ This is the setter function for width """
        if type(width) != int:
            raise TypeError("width must be integer")
        if width <= 0:
            raise ValueError("width must be > 0")   
        self.__width = width

    @property
    def height(self):
        """ This is the getter function for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """ This is the setter function for height"""
        if type(height) != int:
            raise TypeError("height must be integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ This is the getter function for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """ This is the setter function for x"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ This is the getter function y"""
        return self.__y

    @y.setter
    def y(self, y):
        """ This is the setter function y"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
