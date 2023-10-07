#!/usr/bin/python3
def multiple_returns(sentence=""):
    n = len(sentence)
    c = None
    if n:
        c = sentence[0]

    tuple_a = (n, c)
    return (tuple_a)
