#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """a function that returns a new dictionary with all values
    multiplied by 2

    Arguments:
        a_dictionary: the dictionary

    Return: a new dictionary
    """
    my_dict = {}
    for key, value in a_dictionary.items():
        my_dict[key] = value ** 2
    return my_dict
