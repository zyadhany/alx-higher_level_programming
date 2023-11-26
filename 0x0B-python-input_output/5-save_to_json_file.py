#!/usr/bin/python3

import json


"""Documentation of file"""


def save_to_json_file(my_obj, filename):
    """Documentation of function"""
    with open(filename, "w") as fn:
        json.dump(my_obj, fn)
