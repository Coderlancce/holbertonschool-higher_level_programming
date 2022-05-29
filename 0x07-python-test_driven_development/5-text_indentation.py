#!/usr/bin/python3
"""
The text_indentation module
===========================
this module has a text_indentation fucn just for now
"""


def text_indentation(text):
    """
    Funtion that replace "." and "?" by 2 "\n" and print it.
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    for i in [".", "?", ":"]:
        text = text.replace(i, i + "\n\n")
    print("\n".join(x.strip() for x in text.split("\n")), end="")
