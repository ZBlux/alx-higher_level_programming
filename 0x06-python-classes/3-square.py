#!/usr/bin/python3
"""Square class square.py"""


class Square:
    """Represents a square with a private size attribute.

    Attributes:
        __size (int): The size of a side of the square.
    """

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int): The size of a side of the square. Defaults to 0.

        Raises:
            TypeError: If 'size' is not an integer.
            ValueError: If 'size' is less than 0.
        """
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """Calculate the area of the square.
        Returns:
            The area of the square, calculated by size squared.
        """

        return(self.__size ** 2)
