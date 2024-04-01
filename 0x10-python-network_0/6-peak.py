#!/usr/bin/python3

''' get peak '''


def find_peak(list_of_integers):
    ''' get peak func '''

    if not list_of_integers or len(list_of_integers) == 0:
        return (None)

    return max(list_of_integers)
