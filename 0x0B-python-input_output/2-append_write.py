#!/usr/bin/python3


"""Documentation of file"""


def write_file(filename="", text=""):
    """Documentation of function"""

    with open(filename, "w", encoding="utf-8") as fn:
        return fn.write(text)
