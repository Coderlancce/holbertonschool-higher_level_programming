#!/usr/bin/python3
"""
Math operations module
=======================
This module adds 2 integers
"""


def add_integer(a, b=98):
    """
    That function adds 2 integers or floats, no more
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    a = int(a) if type(a) != int else a
    b = int(b) if type(b) != int else b

    return a + b
