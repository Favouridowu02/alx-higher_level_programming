#!/usr/bin/python3
"""
    This Module Contains a Function that returns True if the object is
    an instance of a class that inherited (directly or indirectly) from
    the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
        This Functin returns true if the obj is an instance of the
        class a_class

        Arguments:
            obj: The instance of the object to check
            a_class: The Class

        Return: returns true if obj is an instance else false
    """

    return (isinstance(obj, a_class) and type(obj) != a_class)
