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
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            answer_list = {}

            for count_inp in range(len(attrs)):
                for count_out in obj:
                    if attrs[count_inp] == count_out:
                        answer_list[cunt_out] = obj[count_out]

            return answer_list

        return obj
