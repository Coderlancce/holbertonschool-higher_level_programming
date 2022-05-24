#!/usr/bin/python3
"""Write a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Module __init__ for size square validation"""
        if type(size) not is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

        if type(position) != tuple or \
           not all(type(x) == int for x in position) or \
           not all(x >= 0 for x in position) or \
           len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self._Square__position = position

    def area(self):
        """ return the current square area """
        return self._Square__size ** 2

    @property
    def size(self):
        """ retrieve the size of Square obj """
        return self._Square__size

    @size.setter
    def size(self, value):
        """ set the size of Square obj """
        self.__init__(value, self.position)

    def my_print(self):
        """ draw in stdout the square with the character # """
        [print() for x in range(self.position[1])]
        print("\n".join(["".join(([" "] * self.position[0]) +
                                 ["#" for x in range(self.size)])
                         for y in range(self.size)]))

    @property
    def position(self):
        """ retrieve the position of Square obj """
        return self._Square__position

    @position.setter
    def position(self, value):
        """ set the position of Square obj """
        self.__init__(self.size, value)
