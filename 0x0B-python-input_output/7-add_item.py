#!/usr/bin/python3
""" script that adds all arguments to a Python list,
and then save them to a file """
from os import path
from sys import argv as av


load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

if __name__ == "__main__":
    fileAdd = "add_item.json"
    buff = []

    if path.isfile(fileAdd):
        buff = load_from_json_file(fileAdd)

    buff.extend(av[1:])
    save_to_json_file(buff, fileAdd)
