#!/usr/bin/python3
"""Module for (de)serializing CustomObject instances using pickle."""

import pickle


class CustomObject():
    """A class representing a custom object with serialization capabilities."""

    def __init__(self, name, age, is_student):
        """ Initialize a CustomObject instance."""

        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """Serialize the CustomObject instance to a file using pickle."""

        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    def display(self):
        """Display the attributes of the CustomObject instance."""

        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"is_student: {True if self.is_student else False}")

    @classmethod
    def deserialize(cls, filename):
        """Deserialize a CustomObject instance from a file using pickle."""

        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None
