#!/usr/bin/python3
"""
Write a class BaseGeometry (based on 6-base_geometry.py)
"""


class BaseGeometry:
    """ class BaseGeometry """

    def area(self):
        """ incomplepublic class method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ func that validates value """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
