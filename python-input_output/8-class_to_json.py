#!/usr/bin/pyton3
"""Create a function that return a dictionary description"""


def class_to_json(obj):
    """Returns dictionary description for JSON serialization"""
    result = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[key] = value

    return result
