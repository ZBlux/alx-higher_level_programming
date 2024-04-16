#!/usr/bin/python3
"""
function that returns list of available attributes and methods of an object
"""


def lookup(obj):
    """Returns a list of attributes and methods of the given object."""
    return dir(obj)
