#!/usr/bin/python3
"""
Module 0-add_integer
Contient une fonction pour additionner deux entiers
"""

def add_integer(a, b=98):
    """
    Adds two integers.
    
    Args:
        a: First number (integer or float)
        b: Second number (integer or float), defaults to 98
        
    Returns:
        Integer: The sum of a and b converted to integers
        
    Raises:
        TypeError: If a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
