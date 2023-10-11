#!/usr/bin/python3
def best_score(a_dictionary={}):
    if not a_dictionary:
        return (None)

    mx = 0
    for key, value in a_dictionary.items():
        mx = max(mx, value)
    return (mx)
