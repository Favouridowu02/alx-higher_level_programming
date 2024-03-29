#!/usr/bin/python3
"""
    This Module contains a Base Class Module
"""
import json
import csv
import turtle


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
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.
        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                rec = cls(1, 1)
            else:
                rec = cls(1)
            rec.update(**dictionary)
            return rec

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances
        Args:
            None
        <class name>,json must exist
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, mode="r", encoding="UTF-8") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """
            Return a list of classes instantiated from a csv file
            Reads from `<cls.__name>.csv`
            Returns:
                If the file does not exist - an empty list
                Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r", newline="") as csv_file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_square):
        """
            Draw Rectangles and Square using the turtle module
        Args:
            list_rectangles (list): A list of Rectangle objects to draw
            list_squares (list): A list of Square obects to draw
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
