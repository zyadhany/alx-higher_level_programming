#!/usr/bin/python3

"""Documentation of file"""


def pascal_triangle(n):
    """Documentation of function"""

    if n <= 0:
        return []

    res = [[1]]

    for i in range(1, n):
        res.append([1])
        for j in range(1, i):
            re = res[i - 1][j] + res[i - 1][j - 1]
            res[i].append(re)
        res[i].append(1)

    return (res)
