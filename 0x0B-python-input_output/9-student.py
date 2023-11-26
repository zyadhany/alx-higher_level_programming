#!/usr/bin/python3

"""Documentation of file"""


class Student:
    """Documentation of function"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


def to_json(obj):
    """Documentation of function"""
    return obj.__dict__
