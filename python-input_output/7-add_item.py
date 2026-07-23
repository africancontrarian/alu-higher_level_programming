#!/usr/bin/python3
"""Adds all command line arguments to a list and saves that list
as a JSON representation in add_item.json."""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
