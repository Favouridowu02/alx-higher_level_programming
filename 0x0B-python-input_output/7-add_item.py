#!/usr/bin/python3
"""
    This module contains a script that adds all arguments to a Python list,
    and then save them to a file
"""


import json
from sys import argv

filename = "add_item.json"
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

try:
    text = load_from_json_file(filename)
except FileNotFoundError:
    text = []

for arg in argv[1:]:
    text.append(arg)

save_to_json_file(text, filename)
