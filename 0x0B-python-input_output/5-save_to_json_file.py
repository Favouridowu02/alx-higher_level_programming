#!/usr/bin/python3
"""
    This Module contains a function that writes an Object to a text file,
    using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """
        This function writes an Object to a text file, using a
        JSON representation
    """
    import json
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
