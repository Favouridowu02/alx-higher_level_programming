#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """ a function that prints x elements of a list.

    Arguments:
        my_list: the list
        x: the number of elements to be printed out

    Return: the real number of elements printed
    """
    i = 0

    while i < x:
        try:
            print("{}".format(my_list[i]), end="")
            i += 1
        except IndexError:
            break
    print()
    return i
