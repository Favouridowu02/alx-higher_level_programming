#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """ a function that divides element by element 2 lists.

    Argument:
        my_list_1: the first list
        my_list_2: the second list
        list_length: the number of elements to be printed out

    Return: new list (length = list_length) with all divisions
    """
    while len(my_list_1) < list_length:
        my_list_1.append(0)
    while len(my_list_2) < list_length:
        my_list_2.append(0)

