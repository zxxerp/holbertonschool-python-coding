#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Class that defines a square."""

    def __init__(self, size=0):
        """Initialize square with size."""
        self.size = size

    @property
    def size(self):
        """Retrieve size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of square."""
        return self.__size * self.__size

    def my_print(self):
        """Print square with # character."""
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__size):
            print("#" * self.__size)
