#!/usr/bin/python3
def best_score(a_dictionary):
    """ a function that returns a key with the biggest integer value

    Arguments:
        a_dictionary: the dictionary

    Return: returns None If no score found
    """
    if a_dictionary:
        num = 0
        dict_key = None
        for key, value in a_dictionary.items():
            if (num < value):
                num = value
                dict_key = key
        return dict_key
    return None
