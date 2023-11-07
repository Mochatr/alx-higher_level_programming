#!/usr/bin/python3


import json


def save_to_json_file(my_obj, filename):
    """ Writes an object to a text file
    using a JSON representation

    Args:
        my_obj: object
        filename: file
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)