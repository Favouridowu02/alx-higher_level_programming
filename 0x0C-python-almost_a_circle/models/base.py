#!/usr/bin/python3
"""
    This Module contains a Base Class Module
"""


class Base:
    """
        This is the base Module of the project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            This is the initialization of the Base Model Class

            Argument:
                id: the Id
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
