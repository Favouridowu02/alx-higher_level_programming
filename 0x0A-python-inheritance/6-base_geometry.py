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
