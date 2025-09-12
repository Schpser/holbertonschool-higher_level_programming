#!/usr/bin/python3
"""
Module 3-say_my_name
Contains function to print name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>

    Args:
        first_name: first name string
        last_name: last name string (optional)

    Raises:
        TypeError: if first_name or last_name are not strings
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
