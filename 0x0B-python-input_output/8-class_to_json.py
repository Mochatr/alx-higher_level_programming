#!/usr/bin/python3
"""Define the method"""


def class_to_json(obj):
    """
    returns the dictionary with simple data structure

    Args:
        obj: object
    """
    return obj.__dict__
