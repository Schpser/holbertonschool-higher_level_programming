#!/usr/bin/python3
"""Create an object from JSON file"""
import json

def load_from_json_file(filename):
    """Creates an object to a text file using JSON"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
