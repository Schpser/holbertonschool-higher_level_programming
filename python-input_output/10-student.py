#!/usr/bin/python3
"""Write a class Student that defines a student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if attrs is None or not isinstance(attrs, list):
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }

        result = {}
        if 'first_name' in attrs:
            result['first_name'] = self.first_name
        if 'last_name' in attrs:
            result['last_name'] = self.last_name
        if 'age' in attrs:
            result['age'] = self.age

        return result
