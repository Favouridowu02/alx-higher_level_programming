#!/usr/bin/python3

"""
    This Module Contains a function that returns the list of avaliable
    methods of the object obj
"""

def lookup(obj):
    """
        This Function returns the list of available attributes and
        methods of an object "obj"
    """
    return dir(obj)
