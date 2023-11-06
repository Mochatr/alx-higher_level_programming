#!/usr/bin/usr/python3
""" Module for the lookup method """


def lookup(obj):
    """ 
    Returns the list of available attributes and methods
    of an object.
    
    Args:
        obj: Object

    Returns:
        list: List of attributes and methods of an object.
    """
    return dir(obj)

