#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """ a function that replaces an element in a list at
    a specific position without modifying the original list

    Arguments:
        my_list: the list
        idx: the index
        element: the element to be replaced with
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    list_cpy = my_list.copy()
    list_cpy[idx] = element
    return list_cpy
