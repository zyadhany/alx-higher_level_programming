#!/usr/bin/python3

''' get peak '''


def find_peak(X):
    ''' get peak func '''

    if not X or len(X) == 0:
        return (None)

    left = 0
    r = len(X) - 1

    while left < r:
        at = (left + r) // 2

        if r == left + 1:
            return max(X[left], X[r])

        if X[at] <= X[left]:
            r = at
        elif X[at] <= X[r]:
            left = at
        elif X[at] >= X[at - 1]:
            left = at
        elif X[at] >= X[at + 1]:
            r = at
        else:
            r = at - 1

    return X[left]
