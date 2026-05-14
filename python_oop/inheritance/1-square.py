#!/usr/bin/env python3
"""Module that defines a Square class that inherits from Rectangle"""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square that inherits from Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        self.__size * self.__size
