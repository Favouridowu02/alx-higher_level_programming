#!/usr/bin/python3
"""
    This module contains a function that appends a string at the end of a
    text file (UTF8) and returns the number of characters
"""


def append_write(filename="", text=""):
    """
        This is a function that appends a string at the end of a
        text file (UTF8) and returns the number of characters
    """
    with open(filename, mode="a", encoding="utf-8") as fi:
        f.write(text)
    return len(text)
