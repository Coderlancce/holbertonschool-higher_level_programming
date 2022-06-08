#!/usr/bin/python3
""" class to json """


def class_to_json(obj):
    """ function that display a dictionary of properties of a inheritance
    to be exportes to JSON File """
    infoDic = {}
    if hasattr(obj, "__dict__"):
        infoDic = obj.__dict__.copy()
    return infoDic
