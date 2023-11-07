#!/usr/bin/python3
"""Define method"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file(UTF8)

    Args:
        filename: file
        text: text to write to the file

    Returns:
        The number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
