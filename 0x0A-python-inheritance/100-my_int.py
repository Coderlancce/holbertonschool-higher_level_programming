#!/usr/bin/python3
""" class MyInt that inherits from int """


class MyInt(int):
    """ a rebel int inherited class """
    def __eq__(self, other):
        """ a == b but reversed """
        return super().__ne__(other)

    def __ne__(self, other):
        """ a != b but reversed """
        return super().__eq__(other)
