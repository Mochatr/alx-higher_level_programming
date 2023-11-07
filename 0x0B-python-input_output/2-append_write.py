#!/usr/bin/python3
"""Define the method"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file
    (UFT8)

    Args:
        filename: file
        text: the text to write to the file

    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
