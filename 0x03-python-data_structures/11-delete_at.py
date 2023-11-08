#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """a function that deletes the item at a specific position
    in a list.

    Arguments:
        my_list: the list
        idx: the index
    Return: returns the updated list
    """

    if my_list:
        del my_list[idx]
    return my_list
