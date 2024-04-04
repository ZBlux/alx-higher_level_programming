#!/usr/bin/python3
"""Square class square.py"""


class Square:
    """
    Attributes:
        __size (int): Private instance attribute
    """
    def __init__(self, size=0):
        """
        Args:
            size: size and must be an int
        """
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
