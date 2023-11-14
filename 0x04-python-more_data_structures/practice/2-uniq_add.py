#!/usr/bin/python3
from functools import reduce
def uniq_add(my_list=[]):
    """a function that adds all unique integers in a list

    Arguments:
        my_list: the list

    Return: return the sum
    """
    my_set = set(my_list)
    return reduce(lambda x, y: x + y, my_set)
