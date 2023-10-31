#!/usr/bin/python3
"""Define a class rectangle."""


class Rectangle:
    """Class that defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializing the rectangle with width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the rectangle's width."""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the rectangle's height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
