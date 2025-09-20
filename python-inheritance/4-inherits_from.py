#!/usr/bin/python3
"""Module documentation"""


def inherits_from(obj, a_class):
    """Check if object inherits from specified class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
