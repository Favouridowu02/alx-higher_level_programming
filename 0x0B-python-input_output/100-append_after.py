#!/usr/bin/python3
"""
    This module contains a function that inserts a line of text to a file
    after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
        This is a function that inserts a line of text to a file, after
        each line containing a specific string

        appends "new_string" after a line containing
            "search_string" in "filename"
    """
    with open(filename, mode="r", encoding="UTF-8") as f:
        line_list = []
        for line in f.readlines():
            line_list.append(line) if line != "" else "break"
            if search_string in line:
                line_list.append(new_string)

    with open(filename, mode="w", encoding="UTF-8") as f:
        f.writelines(line_list)
