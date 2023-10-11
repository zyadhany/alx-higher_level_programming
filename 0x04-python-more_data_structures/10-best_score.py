#!/usr/bin/python3
def best_score(a_dictionary={}):
    if not a_dictionary:
        return (None)

    mx = 0
    s = ""
    for key, value in a_dictionary.items():
        if value > mx:
            mx = value
            s = key
    return (s)
