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

    def area(self):
        """
            This method return the area of the rectangle
        """
        area = self.height * self.width
        return area

    def display(self):
        """
            prints in stdout the Rectangle instance with the character #
        """
        width = self.__width
        height = self.__height
        x = self.__x
        y = self.__y

        for i in range(0, y):
            print()
        for i in range(0, height):
            print(" " * x, end="")
            print("#" * width)

    def __str__(self):
        """
            This is the string representation of the class
        """

        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
               self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
        Args:
            *args(ints): New attribute values

            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
            
            **kwargs(dict): New key/value pairs of attributes
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Retun the dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
