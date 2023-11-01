#!/usr/bin/python3
"""Defines a rectangle class"""


class Rectangle:
    """This class defines a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initializes a new rectangle.

        Args:
            width: the rectangle's width
            height: the rectangle's height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
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
        if not isinstance(value, int):
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
        return (2 * (self.__width + self.__height)

    def __str__(self):
    """Returns the rectangle's representation"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = []
        for a in range(self.__height):
            [rectangle.append("#") for b in range(self.__width)]
            if a != self.__height - 1:
                rectangle.append("\n")
        return "".join(rectangle)

    def __repr__(self):
        """Returns the string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
