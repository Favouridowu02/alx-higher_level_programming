#!/usr/bin/python3
"""
   This module contains a script that adds all arguments to a Python
   list, and then save them to a file
"""

filename = "add_json.py"

from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    text = load_from_json_file(argv)
except:
    text = []

for arg in argv:
    text.append(arg)

save_to_json_file(text, "add_json")
