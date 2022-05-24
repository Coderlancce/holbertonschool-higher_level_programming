#!/usr/bin/python3
"""Write a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Module __init__ for size square validation"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Method position return the position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Method position setter evalue the errors"""
        if (type(value) != tuple or len(value) != 2 or type(value[0]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[1]) != int or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Method area return the square Area"""
        return self.__size ** 2

    def my_print(self):
        """Method my_print print a square"""
        if self.__size > 0:
            for x in range(self.position[1]):
                print("")
            for x in range(self.__size):
                for y in range(self.__position[0]):
                    print(" ", end="")
                for y in range(self.__size):
                    print("#", end="")
                print("")
        print("")
