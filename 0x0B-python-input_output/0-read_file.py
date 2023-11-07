#!/usr/bin/python3
"""define the method"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename: The file to read
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())
