#!/usr/bin/python3
"""Write a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Module __init__ for size square validation"""
        self.size = size

    @property
    def size(self):
        """Method property of size and return the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Method size_setter atributte evaluate the value"""
        if type(value) is not int:
            raise TypeError("size must be an integrer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Method area return the square Area"""
        return self.__size ** 2
