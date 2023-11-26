#!/usr/bin/python3


"""Documentation of file"""


def write_file(filename="", text=""):
    """apped text to file

    Args:
        filename (str): file name.
        text (str): text to append.
    Returns:
        number of characters that appended.
    """
    
    with open(filename, "w", encoding="utf-8") as fn:
        return fn.write(text)
