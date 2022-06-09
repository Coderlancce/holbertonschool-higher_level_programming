#!/usr/bin/python3
""" create a class student """


class Student:
    """ Class Student that defines a Student obj """

    def __init__(self, first_name, last_name, age):
        """ Class Student constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method that returns directory description """
        answer_list = {}
        if type(attrs) is list:
            if all(type(i) is str for i in attrs):
                for item in attrs:
                    if hasattr(self, item):
                        answer_list[item] = getattr(self, item)

                return answer_list

        return self.__dict__
