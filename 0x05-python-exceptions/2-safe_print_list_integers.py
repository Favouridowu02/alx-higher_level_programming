#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """ a function that prints x elements of a list.

    Arguments:
        my_list: the list
        x: the number of elements to be printed out

    Return: the real number of elements printed
    """
    i = 0
    k = 0

    while k < x:
        try:
            if type(my_list[k]) is int:
                print("{:d}".format(my_list[k]), end="")
                i += 1
            k += 1
        except NameError:
            break
    print()
    return i
