#!/usr/bin/python3
""" create a Base class """
import json


class Base:
    """ Base class """
    __nb_objects = 0
    
    def __init__(self, id=None):
        """ Base class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ representation of list dictionaries """
        
