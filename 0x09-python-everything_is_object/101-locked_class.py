#!/usr/bin/python3
""" This moduule contains a class which only gives the previledge of using
the first_name attribute using __slots__
"""


class LockedClass:
    """  prevents the user from dynamically creating new instance attributes
    except if the new instance attribute is called first_name.
    """
    __slots__ = ["first_name"]
