#!/usr/bin/env python3
"""Module that defines a function to write text to a file."""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        contenu = f.write(text)
    return contenu
