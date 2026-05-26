#!/usr/bin/env python3
"""Module that defines a function to read and print a text file."""


def read_file(filename=""):
    """Reads a text file and prints its content to stdout."""
    with open(filename, encoding="utf-8") as f:
        contenu = f.read()
        print(contenu)
