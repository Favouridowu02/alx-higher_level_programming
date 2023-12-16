#!/usr/bin/python3

"""
    This Module Contains a function that prints the integers
    in the list in an ascending order
"""


class MyList(list):
    """
        This class that prints the integer in the list
        in an ascending order by inheriting the list
    """

    def __init__(self):
        """ The Initialiazation to be ran when the file is created"""
        super().__init__()

    def print_sorted(self):
        """
            This function re-order the list above
        """
        new_list = sorted(self)
        print(new_list)
