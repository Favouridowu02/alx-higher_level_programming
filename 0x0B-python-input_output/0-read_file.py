#!/usr/bin/python3
"""
    This module contains a function that reads a text file in utf-8
    and prints it to the stdout
"""


def read_file(filename=""):
    """
        This function reads a text file in utf-8 and prints it to the std
        output
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        for i in f.readlines():
            print(i, end="")
