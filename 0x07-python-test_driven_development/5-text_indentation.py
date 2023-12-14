#!/usr/bin/python3
"""
    This Module contains a function that prints a text with 2 lines after
    each of these characters '.', '?' and ':'
"""


def text_indentation(text):
    """ 
    a function that prints a text with 2 lines after each of these
    characters '.', '?' and ':'

    Arguments:
        text: the text argument to be passed

    Return: None
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in text:
        print(i, end="")
        if i in ['.', '?', ':']:
            print()
