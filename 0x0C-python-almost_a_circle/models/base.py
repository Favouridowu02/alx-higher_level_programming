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
        import json
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON serialization of a list of objects to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode="w+", encoding="UTF-8") as f:
            if f is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary for o in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the deserialization of a JSON string.
        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]"
            return []
        return json.loads(json_string)

