#!/usr/bin/python3
"""
script that adds all arguments to a Python list,
and then save them to a file
"""


from os import path
from sys import argv as av

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

buff = []

if path.isfile("add_item.json") is False:
    save_to_json_file(buff, "add_item.json")

buff = load_from_json_file("add_item.json")

if sys.av[1:]:
    for i in sys.av[1:]:
        buff.append(i)

save_to_json_file(buff, "add_item.json")
