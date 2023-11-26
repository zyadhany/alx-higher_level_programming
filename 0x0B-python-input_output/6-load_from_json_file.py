#!/usr/bin/python3

"""Documentation of file"""


import json


def load_from_json_file(filename):
    """Documentation of function"""
    with open(filename) as f:
        return json.load(f)
