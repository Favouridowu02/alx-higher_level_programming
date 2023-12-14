#!/usr/bin/python3
"""
    This module contains a function that prints the users name
"""


def say_my_name(first_name, last_name=""):
    """ 
        This function prints the user first name and last name
        
        Arguments:
            first_name: the first parameter contains the user first name
            last_name: the last parameter contains the user last name

        Return: None
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    
    print("My name is {} {}".format(first_name, last_name))
