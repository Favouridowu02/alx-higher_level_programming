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
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ This is the getter function for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """ This is the setter function for width """
        self.__width = width

    @property
    def height(self):
        """ This is the getter function for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """ This is the setter function for height"""
        self.__height = height

    @property
    def x(self):
        """ This is the getter function for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """ This is the setter function for x"""
        self.__x = x

    @property
    def y(self):
        """ This is the getter function y"""
        return self.__y

    @y.setter
    def y(self, y):
        """ This is the setter function y"""
        self.__y = y

