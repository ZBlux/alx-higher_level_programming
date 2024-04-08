#!/usr/bin/python3
"""Module 0-rectangle
Defines a class Rectangle.
"""


class Rectangle:
    """
    A class that defines a rectangle.
    Attributes:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle with optional width and height.
        Args:
            width (int, optional): width of rectangle. Defaults to 0.
            height (int, optional): height of rectangle. Defaults to 0.
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Print a message when a Rectangle instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Get the width of the rectangle.
        Returns:
            int: the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.
        Args:
            value (int): width of the rectangle.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle.
        Returns:
            int: the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.
        Args:
            value (int): height of the rectangle.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Calculates area of a rectangle.

        Returns:
            int: area
        """
        return self.__width*self.__height

    def perimeter(self):
        """Calculates perimeter of a rectangle
        Returns:
            int: perimeter.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """Prints the rectangle with the character #.
        Returns:
            str: the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = ""
        for h in range(self.__height):
            for w in range(self.__width):
                rect_str += "#"
            if h != self.__height - 1:
                rect_str += "\n"
        return rect_str

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)
