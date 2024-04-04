#!/usr/bin/python3
"""Square class square.py"""


class Square:
    """
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """
        Args:
            size: size and must be an int
        Raises :
            TypeError: size not int
            ValueError: size < 0
        """
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
    def area(self):
        """
        area of square:
            Returns:
                size**2 or size*size
        """
        return(self.__size ** 2)
