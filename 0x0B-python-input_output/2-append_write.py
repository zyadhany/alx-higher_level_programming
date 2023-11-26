#!/usr/bin/python3


"""Documentation of file"""


def append_write(filename="", text=""):
    """apped text to file"""

    with open(filename, "a", encoding="utf-8") as fn:
        return fn.write(text)
