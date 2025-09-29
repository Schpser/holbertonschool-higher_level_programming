#!/usr/bin/python3
"""JSON deserialization module"""
import json


def from_json_string(my_str):
    """Returns object from JSON string"""
    return json.loads(my_str)
