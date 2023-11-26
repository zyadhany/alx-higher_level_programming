#!/usr/bin/python3


"""Documentation of file"""


def write_file(filename="", text=""):
    """apped text to file"""
    
    with open(filename, "w", encoding="utf-8") as fn:
        return fn.write(text)
