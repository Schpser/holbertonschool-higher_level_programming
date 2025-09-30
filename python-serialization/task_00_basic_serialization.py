#!/usr/bin/python3
"""Function to be (De)serialized"""

import json


def serialize_and_save_to_file(data, filename):
    """ Serializes the given data to JSON format and saves it to a file. """
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Data serialized and saved to '{filename}'.")


def load_and_deserialize(filename):
    """ Loads and deserializes JSON data from a file. """
    with open(filename, "r") as f:
        data = json.load(f)
    return data
