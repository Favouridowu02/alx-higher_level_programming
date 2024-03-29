#!/usr/bin/python3
"""
    This module contains a function that creates an Object from a
    “JSON file”
"""


def load_from_json_file(filename):
    """
        This function creates an Object from a “JSON file”
    """
    import json
    with open(filename, "r", encoding="utf-8") as f:
        return (json.load(f))
