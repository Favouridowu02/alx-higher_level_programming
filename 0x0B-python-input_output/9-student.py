#!/usr/bin/python3
"""
    This module contains a class that defines a student by:

    Public instance attributes:
        first_name: FIrst Name
        last_name: Last Name
        age: The Age

    Return: None
"""


class Student:
    """
        This class that defines a student by:

        Public instance attributes:
            first_name: FIrst Name
            last_name: Last Name
            age: The Age

        Method:
            to_json: retrieves a dictionary representation of a Student
            instance

        Return: None
    """

    def __init__(self, first_name, last_name, age):
        """
            This is just the initialization of the Class Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            This method retrieves a dictionary representation of a Student
            Instances
        """
        return self.__dict__
