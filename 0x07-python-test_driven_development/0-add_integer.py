#!/usr/bin/python3
"""
This module provides a function to add two integers or floats.
The result is an integer.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the sum as an integer.

    Args:
        a (int/float): The first number.
        b (int/float, optional): The second number. Defaults to 98.

    Raises:
        TypeError: If either of a or b is neither an integer nor a float.

    Returns:
        int: The sum of a and b after casting them to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
