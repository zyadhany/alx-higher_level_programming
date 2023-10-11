#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    X = list(a_dictionary.keys())
    X.sort()
    for m in X:
        print("{}: {}".format(m, a_dictionary[m]))
