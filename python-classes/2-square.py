#!/usr/bin/python3

''' Create a Square instance that defines a Square '''
class Square:
    """Define a Square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")