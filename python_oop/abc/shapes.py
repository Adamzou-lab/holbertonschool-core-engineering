#!/usr/bin/env python3
"""Module that defines abstract Shape class with
Circle and Rectangle implementations"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class representing a shape"""
    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    """Concrete class representing a circle"""
    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete class representing a rectangle"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    print(shape.area())
    print(shape.perimeter())


circle = Circle(5)
rectangle = Rectangle(2, 3)

shape_info(circle)
shape_info(rectangle)
