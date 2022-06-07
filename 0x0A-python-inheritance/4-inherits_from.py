#!/usr/bin/python3
"""
inherited class
"""


def inherits_from(obj, a_class):
    """
    checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    """
    return False if type(obj) is a_class else isinstance(obj, a_class)
