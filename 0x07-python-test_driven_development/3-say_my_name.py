#!/usr/bin/python3
"""
Math operations module
=======================
Write a complete name
"""


def say_my_name(first_name, last_name=""):
    """
    Funtion that prints a presentation
    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    for character in first_name:
        if character.isdigit():
            raise TypeError("first_name must be a string, no numbers")
    for character in last_name:
        if character.isdigit():
            raise TypeError("last_name must be a string, no numbers")

    print("My name is {} {}".format(first_name, last_name))
