#!/usr/bin/python3
""" Module """


def is_same_class(obj, a_class):
    """
    Verifies wheteher the object is exactly an instance
    of the specified class.
    """
    return obj.__class__ is a_class
