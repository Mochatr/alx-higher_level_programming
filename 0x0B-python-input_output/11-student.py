#!/usr/bin/python3
"""class"""


class Student:
    """A class that defines a student"""
    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a student
        instance"""
        if attrs is None:
            return self.__dict__
        return {attr: getattr(self, attr)
                for attr in attrs if hasattr(self, atr)}

    def reload_from_json(self, json):
        """Replaces all the attributes of the student instance"""
        for key, value in json.items():
            setattr(self, key, value)
