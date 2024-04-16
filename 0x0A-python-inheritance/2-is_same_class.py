#!/usr/bin/python3
"""
function that returns True
if the object is exactly an instance of the specified class
otherwise False
"""


def is_same_class(obj, a_class):
    """
    Args:
        obj: The object to check.
        a_class: The class type to compare against.

    Returns:
        bool: True if obj is an instance of class_type, else False.
    """
    return (type(obj) == a_class)
