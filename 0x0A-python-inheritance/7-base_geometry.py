#!/usr/bin/python3
"""
    This Module Contains a class called Base Geometry that raises an error
"""


class BaseGeometry:
    """
        This class raises an Exception
    """
    def __init__(self):
        """ This is the Initialization of the Class"""
        pass

    def area(self):
        """
            This function is to raise the error
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This Function validates value

        Arguments:
            name: is always a string
            value: is meant to be an integer

        Return: None
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater tham 0".format(name))
