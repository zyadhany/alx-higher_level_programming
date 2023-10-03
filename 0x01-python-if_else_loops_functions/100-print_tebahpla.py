#!/usr/bin/python3
for i in range(97, 123):
    a = 123 - i + 96
    if a % 2:
        a -= 32
    print("{}".format(chr(a)), end="")
