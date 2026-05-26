#!/usr/bin/env python3
"""Module that defines a function to append text to a file."""


def append_write(filename="", text=""):
    """Appends a string to a text file and returns
    the number of characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        contenu = f.write(text)
    return contenu
