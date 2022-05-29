#!/usr/bin/python3
"""
The square print module
=======================
this module has a print_square fucn just for now
"""


def print_square(size):
    """
    Funtion that prints a square with "#" according to size
    """

    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    print("\n".join(["#" * size] * size))
