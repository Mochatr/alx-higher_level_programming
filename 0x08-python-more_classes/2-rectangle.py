#!/usr/bin/python3
"""Defines a class Rectangle."""


class Rectangle:
    """A class that defines a Rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle.

        Args:
            width: The width of the new rectangle
            height: The height of the new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle's area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle's perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
