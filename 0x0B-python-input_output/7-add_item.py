#!/usr/bin/python3
"""
script that adds all arguments to a Python list,
and then save them to a file
"""

from os import path
from sys import argv as av

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

my_list = []
if os.path.exists("add_item.json"):
    my_list = load_file("add_item.json")

for arg in sys.argv[1:]:
    my_list.append(arg)

save_file(my_list, "add_item.json")
