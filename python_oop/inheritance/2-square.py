#!/usr/bin/env python3
"""Module that defines a Square class that inherits from Rectangle"""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square that inherits from Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
