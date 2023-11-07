#!/usr/bin/python3
"""Define the class"""


class Student:
    """A class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation
        of a student instance
        """
        if attrs is None:
            return self.__dict__

        dictionary = {}
        for key, value in self.__dict__.items():
            if key is attrs:
                dictionary[key] = value

        return dictionary
