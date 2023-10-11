#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    X = list(a_dictionary.keys())

    for n in X:
        if a_dictionary[n] == value:
            del a_dictionary[n]
    return (a_dictionary)
