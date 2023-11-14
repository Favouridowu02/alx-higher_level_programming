#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """a function that replaces all occurrences of an element by
    another in a new list

    Arguments:
        my_list: the initial list
        search: the element to replace in the list
        replace: new element

    Return: The new version of the replaced lis
    """
    my_list_cpy = list(map(lambda x: replace if x == search else x, my_list))
    # my_list_cpy = my_list.copy()
    # for i in my_list_cpy:
    #    if i == search:
    #        my_list_cpy[my_list_cpy.index(i)] = replace
    return my_list_cpy
