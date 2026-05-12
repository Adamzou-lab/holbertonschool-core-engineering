#!/usr/bin/env python3
"""Module that defines a Square class."""


class Square:
    """Represents a square."""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if (not isinstance(position, tuple)
                or len(position) != 2
                or not isinstance(position[0], int)
                or not isinstance(position[1], int)
                or position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = position

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)
