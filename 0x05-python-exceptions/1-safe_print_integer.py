#!/usr/bin/python3
def safe_print_integer(value):
    """ a function that prints an integer with "{:d}".format()

    Arguments:
        value: the integer to be printed out

    Return: True if value has been correctly printed else false
    """
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
