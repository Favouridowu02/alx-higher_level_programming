#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """a function that returns a set of all elements present in only one set

    Arguments:
        set_1: the first set
        set_2: is the second set

    Return: a set of all elements present in only one set.
    """
    return set_1 ^ set_2 # set_1.symmetric_difference(set_2)
