#!/usr/bin/env python3
"""Module that defines a Square class."""


class Square:
    """Represents a square."""
    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
