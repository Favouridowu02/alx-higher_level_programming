#!/usr/bin/python3
"""
    This Module Contains a Class Square which inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        This Class inherits from the Class Rectangle
    """

    def __init__(self, size):
        """
            This is the Instantialization of the Class Square

            Arguments:
                size: the size of the square

            Return: None
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """ This function returns the area of the square """
        return (self.__size ** 2)

    def __str__(self):
        """ This returns a Printable string"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
