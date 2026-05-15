#!/usr/bin/env python3
"""Module that defines abstract Animal class and its concrete subclasses"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Concrete class representing a dog"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Concrete class representing a cat"""
    def sound(self):
        return "Meow"
