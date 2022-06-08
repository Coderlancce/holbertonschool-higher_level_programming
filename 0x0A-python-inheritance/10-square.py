#!/usr/bin/python3
""" import class to inherit for """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class inherited from Reactangle """

    def __init__(self, size):
        """ inizilalice it """
        super().integer_validator("size", size)
        self._Square__size = size
        super().__init__(size, size)

    def area(self):
        """ inherit get area function """
        return super().area()
