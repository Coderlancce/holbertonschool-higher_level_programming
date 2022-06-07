#!/usr/bin/python3
""" import class to inherit for """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle that inherits from """

    def __init__(self, width, height):
        """ Instantiation with width and height """
        super().integer_validator("height", height)
        super().integer_validator("width", width)
        self._Rectangle__height = height
        self._Rectangle__width = width

    def area(self):
        """ return Rectangle area """
        return self._Rectangle__height * self._Rectangle__width

    def __str__(self):
        """ set format print """
        return "[Rectangle] {:d}/{:d}".format(self._Rectangle__width,
                                              self._Rectangle__height)
