#!/usr/bin/python3
def no_c(my_string):
    """a function that removes all characters c add
    C from a string
    my_string: the soure
    """
    char_str = ""
    for i in my_string:
        if i != "c" and i != "C":
            char_str += i
    return char_str
