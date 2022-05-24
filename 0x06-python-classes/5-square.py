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
        return (self.__size)

    @size.setter
    def size(self, value):
        """Method size_setter atributte evaluate the value"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Method area return the square Area"""
        return self.__size ** 2 

    def my_print(self):
        """Method my_print print a square"""
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
