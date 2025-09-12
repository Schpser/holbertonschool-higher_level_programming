#!/usr/bin/python3
"""
Module 0-add_integer
Contains a function that add two integers
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number, defaults to 98.

    Returns:
        int: The integer sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        if a != a:
            raise TypeError("a must be an integer")
        if a in [float('inf'), float('-inf')]:
            raise TypeError("a must be an integer")

    if isinstance(b, float):
        if b != b:
            raise TypeError("b must be an integer")
        if b in [float('inf'), float('-inf')]:
            raise TypeError("b must be an integer")

    return int(a) + int(b)
