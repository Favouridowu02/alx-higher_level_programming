#!/usr/bin/python3
def safe_print_division(a, b):
    """  function that divides 2 integers and prints the result

    Arguments:
        a: the first integer
        b: the second integer

    Return: the value of the division, otherwise: None
    """
    try:
        a = int(a)
        b = int(b)
        result = a / b
        return result
    except Exception:
        result = None
        return None
    finally:    
        print("Inside result: {}".format(result))
