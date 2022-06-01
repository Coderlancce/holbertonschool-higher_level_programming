#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle
"""


class Rectangle:
    """ class Rectangle that defines a rectangle """

    def __init__(self, width=0, height=0):
        """ set properties to instance """
        self.height = height
        self.width = width

    def __testInput(self, prop, value):
        """ test width and heigh inputs """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(prop))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(prop))
        return True

    @property
    def width(self):
        """ width getter """
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """ width setter """
        if self.__testInput("width", value):
            self._Rectangle__width = value

    @property
    def height(self):
        """ height getter """
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """ height setter """
        if self.__testInput("height", value):
            self._Rectangle__height = value
