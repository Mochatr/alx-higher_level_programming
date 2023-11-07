#!/usr/bin/python3
""" Module for the Rectangle class """
from 7-base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """ Thins class inherites BaseGeometry """
    def __init__(self, width, height):
        """ Constructor """
        super().__init()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Method """
        return (self.__width * self.__height)

    def __str__(self):
        """ Method """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
