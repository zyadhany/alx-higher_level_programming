#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for n in a_dictionary:
        if a_dictionary[n] == value:
            del a_dictionary[n]
    return (a_dictionary)
