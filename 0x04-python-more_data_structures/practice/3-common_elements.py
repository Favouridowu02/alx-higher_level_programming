#!/usr/bin/python3
def common_elements(set_1, set_2):
    """a function that returns a set of common elements in two sets

    Arguments:
        set_1: the first set
        set_2: the second set

    Return: the common elements
    """
    common_elements =  set_1 & set_2
    #common_elements = set_1.intersection(set_2)
    return common_elements
