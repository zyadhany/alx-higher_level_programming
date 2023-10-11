#!/usr/bin/python3
def weight_average(my_list=[]):
    if not len(my_list):
        return (0)

    a = 0
    b = 0

    for n in my_list:
        a += n[0] * n[1]
        b += n[1]

    return (a / b)
