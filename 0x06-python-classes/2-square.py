#!/usr/bin/python3
"""Write a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Module __init__ for size square validation"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
