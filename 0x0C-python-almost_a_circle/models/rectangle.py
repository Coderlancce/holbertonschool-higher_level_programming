#!/usr/bin/python3
""" Create a class Rectangle from Base """
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

# Cast Errors

    @staticmethod
    def checkInp(name, value, compare):
        """ check if inp fit to class properties """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if not eval("value {} 0".format(compare)):
            raise ValueError("{} must be {} 0". format(name, compare))

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        self.checkInp("width", value, ">")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        self.checkInp("height", value, ">")
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        self.checkInp("x", value, ">=")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        self.checkInp("y", value, ">=")
        self.__y = value

# modifiers methods

    def area(self):
        """ returns the area value of Rectangle instance """
        return self.width * self.height

    def display(self):
        """ prints in stdout the Rectangle instance with the caracter # """
        print("\n" * self.y, end="")
        print("\n".join([" " * self.x + "#" * self.width] * self.height))

# Update class Rectangle

    @property
    def getType(self):
        """ retrives self type """
        return self.__class__.__name__

    def f(self, string):
        """ simulate f-strings available from python """
        return string.format(**locals())

    def __str__(self):
        """ modify instance str output """
        return self.f("[{self.getType}] ({self.id}) {self.x}/{self.y} - "
                      "{self.width}/{self.height}")

# update method

    def update(self, *args, **kwargs):
        """ Update the class Rectangle """
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

# update adding dictiory

    def to_dictionary(self):
        """ dictionary of th elements """
        list_atr = ['id', 'width', 'height', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            dict_res[key] = getattr(self, key)

        return dict_res
