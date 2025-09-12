#!/usr/bin/python3
"""
Module 4-print_square
Contains function to print square with #
"""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        return

    for i in range(size):
        print("#" * size)
