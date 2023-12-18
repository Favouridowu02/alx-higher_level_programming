#!/usr/bin/python3
"""
    This Module Contains a Class Square that inherits from the class Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        This Class Inherits from the class Rectangle
    """
    def __init__(self, size):
        """
            This Function is for the Instantialization of the Class

            Arguments:
                size: The size of the Square

            Return: None
        """
        self.integer_validator("size",size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ This Function returns the area of the square """
        return (self.__size ** 2)
