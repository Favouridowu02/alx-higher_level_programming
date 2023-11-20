#!/usr/bin/python3
def safe_function(fct, *args):
    """ a function that executes a function safely.

    Arguments:
        fct: a pointer to the function
        args: the arguments

    Return: the result of the function
    """
    try:
        result = fct(*args)
        return result
    except Exception as err:
        import sys
        print("Exception: {}".format(err), file=sys.stderr)
        return None
