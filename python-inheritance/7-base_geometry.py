#!/usr/bin/python3
"""BaseGeometry class with area and integer_validator methods"""


class BaseGeometry:
    """A base geometry class"""

    def area(self):
        """Raises an Exception that area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer"""
        if type(value) is not int:
            raise TypeError("test must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
