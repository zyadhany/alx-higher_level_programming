#!/usr/bin/python3

''' get peak '''


def find_peak(X):
    ''' get peak func '''

    if not X or len(X) == 0:
        return (None)

    l = 0
    r = len(X) - 1

    while l < r:
        at = (l + r) // 2

        if X[at] <= X[l]:
            r = at
        elif X[at] <= X[r]:
            l = at
        elif X[at] >= X[at - 1]:
            l = at
        elif X[at] >= X[at + 1]:
            r = at
        else:
            r = at - 1

    return X[l]
