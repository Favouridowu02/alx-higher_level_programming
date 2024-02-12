#!/usr/bin/python3
"""
    This Module contains a function that returns an object (Python data
    structure) represented by a JSON string
"""


def from_json_string(my_str):
    """
        This Function returns an object (Python data structure)
        represented by a JSON string
    """
    import json
    return json.loads(my_str)
