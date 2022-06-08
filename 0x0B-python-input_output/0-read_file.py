#!/usr/bin/python3
""" read text file """


def read_file(filename=""):
    """ read the file input """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
