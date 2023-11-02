#!/usr/bin/python3
""" Module for the add_integer method """


def add_integer(a, b=98):
    """
    Function that adds two integers.

    Args:
        a: First integer.
        b: Second integer.

    Raises:
        TypeError: if a and b aren't integers or floats.

    Returns:
        The sum of two integers.
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return int(a) + int(b)


if __name__ "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
