#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """a function that deletes keys with a specific value in a dictionary.

    Arguments:
        a_dictionary: the dictionary
        value: the value to be deleted

    Return: the edited list
    """
    index = []
    for key in a_dictionary.keys():
        if a_dictionary[key] == value:
            index.append(key)

    for i in index:
        del a_dictionary[i]
    return a_dictionary
