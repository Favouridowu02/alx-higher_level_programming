#!/usr/bin/python3
"""
    This Module Contains a class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        This class inherits from BaseGeomtry
    """
    def __init__(self, width, height):
        """
            This function is used for the instantiation of the class

            Arguments:
                width: the width
                height: the height

            Return: None
        """

        self.__width = width
        self.__height = height

        super().__init__()
        self.integer_validator('width', self.__width)
        self.integer_validator('height', self.__height)

    def area(self):
        """ This returns the area"""
        return (self.__width * self.__height)

    def __str__(self):
        """
            This is for the Printable String
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
