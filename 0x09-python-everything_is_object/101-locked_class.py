#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """A class that prevents new attributes."""

    __slots__ = ["first_name"]
