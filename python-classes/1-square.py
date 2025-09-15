#!/usr/bin/python3

'''Write an empty class Square that defines a square.'''


class Square:
    """Class Square with private instance attribute size"""

    def __init__(self, size):
        """Initialize Square with size
        Args:
            size: size of the square
        """
        self.__size = size
