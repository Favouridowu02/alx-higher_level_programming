#!/usr/bin/python3
"""
    This Module Contains a Function that returns True if the object is
    an instance of, or if the object is an instance of a class that
    inherited from, the specified class; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
        This Functin returns true if the obj is an instance of the
        class a_class

        Arguments:
            obj: The instance of the object to check
            a_class: The Class

        Return: returns true if obj is an instance else false
    """

    return isinstance(obj, a_class)
