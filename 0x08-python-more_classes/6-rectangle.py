#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle
"""


class Rectangle:
    """ class Rectangle that defines a rectangle """

    number_of_instances = 0

# inizialise instance

    def __init__(self, width=0, height=0):
        """ set properties to instance """
        self.height = height
        self.width = width
        self.__class__.number_of_instances += 1

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

# get area and perimeter

    def area(self):
        """ set area of Rectangule instance """
        return self.width * self.height

    def perimeter(self):
        """ set perimeter of Rectangule instance """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

# write Rectangle

    def __str__(self):
        """ draw the Rectangule instance """
        return "\n".join(["#" * self.width] * self.height)

# repr to create a new instance with eval()

    def __repr__(self):
        """ return a string rep, of instance """
        className = self.__class__.__name__
        return "{}({}, {})".format(className, self.width, self.height)

# delet behavior control

    def __del__(self):
        """ print a message after instance delete """
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")
