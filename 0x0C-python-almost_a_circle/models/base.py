#!/usr/bin/python3
"""Defines a base model class."""


class Base:
    """Base class for managing id attribute in future classes."""

    # Private class attribute to keep track of objects
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor.

        Args:
            id (int): the new id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
