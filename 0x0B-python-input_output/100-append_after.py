#!/usr/bin/python3

"""Documentation of file"""


def append_after(filename="", search_string="", new_string=""):
    """Documentation of function"""

    s = ""
    with open(filename) as fn:
        for L in fn:
            s += L
            if search_string in L:
                s += new_string

    with open(filename, "w") as fo:
        fo.write(s)
