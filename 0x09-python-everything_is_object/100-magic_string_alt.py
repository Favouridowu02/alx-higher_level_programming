#!/usr/bin/python3
def magic_string():
    """ a function that returns a string “BestSchool” n times the number of the iteration
    """
    magic_string.count = getattr(magic_string, "count", 0) + 1
    return "BestSchool, " * mic_string.count
