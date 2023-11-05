#!/usr/bin/python3
from add_0 import add
if __name__ == "__main__":
    """Prints the sum of two variables
    Args:
        a: The first interger
        b: The second interger
    """
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b))) 
