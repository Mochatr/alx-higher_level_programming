#!/usr/bin/python3
"""Define the method"""


def to_json_string(my_obj):
    """
    returns the string representation of an object

    Args:
        my_obj: Object to represent as JSON string
    """
    return json.dumps(my_obj)
