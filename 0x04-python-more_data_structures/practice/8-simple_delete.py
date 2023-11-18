#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """a function that deletes a key in a dictionary.

    Arguments:
        a_dictionary: the dictionary
        key: the key of the dictionary to be deleted

    Return: returns the updated version of the dictionary
    """
    a_dictionary.pop(key, None)
    return a_dictionary
