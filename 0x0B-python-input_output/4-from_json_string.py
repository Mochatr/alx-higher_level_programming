#!/usr/bin/python3
"""Define the method"""


import json


def from_json_string(my_str):
    """
    returns an object represented by a JSON string

    Args:
        my_str: string
    """
    return json.loads(my_str)
