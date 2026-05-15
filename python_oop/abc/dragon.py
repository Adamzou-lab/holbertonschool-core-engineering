#!/usr/bin/env python3
"""Module that defines SwimMixin, FlyMixin and Dragon classes using mixins"""


class SwimMixin:
    """Mixin that adds swimming behavior to a class"""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying behavior to a class"""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Concrete class representing a dragon that can swim, fly and roar."""
    def roar(self):
        print("The dragon roars!")


dragon = Dragon()
dragon.swim()
dragon.fly()
dragon.roar()
