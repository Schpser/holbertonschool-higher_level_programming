#!/usr/bin/python3
"""Function that checks if object inherits from a class"""


def inherits_from(obj, a_class):
    """Returns True if obj inherits from a_class, else False"""
    return isinstance(obj, a_class) and type(obj) is not a_class