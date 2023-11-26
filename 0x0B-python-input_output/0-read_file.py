#!/usr/bin/python3

"""print content of file"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as fn:
        print(fn.read(), end="")
