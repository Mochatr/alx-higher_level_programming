#!/usr/bin/python3
""" Module for the the rectangle class """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A subclass that represents a rectangle
    """
    def __init__(self, width, height):
        """ Constructor """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Method
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        A string representation
        """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
