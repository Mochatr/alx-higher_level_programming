#!/usr/bin/python3
""" Define a class """


class Base:
    """ class """
    __nb__objects = 0

    def __init__(self, id=None):
        """ Constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
