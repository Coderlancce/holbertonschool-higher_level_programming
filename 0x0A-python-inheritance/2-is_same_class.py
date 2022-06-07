#!usr/bin/python3
"""
chacks if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    function search exactly on instance of the specified class
    """
    return type(obj) is a_class
