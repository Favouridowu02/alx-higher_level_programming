#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """a function that prints a dictionary by ordered keys

    Arguments:
        a_dictionary: the dictionary

    Return: None
    """
    key = list(a_dictionary.keys())
    key.sort()
    for i in key:
        print("{:s}: {}".format(i, a_dictionary[i]))
    #print(" \n".join(str(a_dictionary[x]) for x in key))
