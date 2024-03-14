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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            A static method that returns the JSON string representation of list_dictionaries

            list_dictionaries: is a list of dictionaries
            If list_dictionaries: is None or empty, return the string: "[]"

            Otherwise, return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    def __str__(self):
