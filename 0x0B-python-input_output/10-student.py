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
        try:
            for attribute in attrs:
                if type(attribute) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        dictionary = dict()
        for key, value in self.__dict__.items():
            if key is attrs:
                dictionary[key] = value
        return dictionary
