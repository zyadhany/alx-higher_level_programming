#!/usr/bin/python3
def uppercase(str):
    for c in str:
        n = ord(c)
        if n >= 97:
            n -= 32
        print("{}".format(chr(n)), end="")
    print("")
