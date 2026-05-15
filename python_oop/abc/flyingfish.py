#!/usr/bin/env python3
"""Module that defines Fish, Bird and FlyingFish classes
with multiple inheritance"""


class Fish:
    """Concrete class representing a fish"""
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """Concrete class representing a bird"""
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Concrete class representing a flying fish that inherits
    from both Fish and Bird"""
    def swim(self):
        print("The flying fish is swimming!")

    def fly(self):
        print("The flying fish is soaring!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")


fish = FlyingFish()

fish.fly()
fish.swim()
fish.habitat()

print(FlyingFish.__mro__)
