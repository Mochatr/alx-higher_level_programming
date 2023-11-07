#!/usr/bin/python3
"""Define the method"""


import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file

    Args:
        filename: file
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f)
