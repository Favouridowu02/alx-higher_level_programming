#!/usr/bin/python3
"""
    This Module contains a funtion that returns the JSON representation
    of an object
"""


def to_json_string(my_obj):
    """
        This function returns the JSON representation of an object
    """
    import json
    return json.dumps(my_obj)
