#!/usr/bin/python3
def uniq_add(my_list=[]):
    summ = 0

    freq = {}

    for i in my_list:
        if not freq.get(i, 0):
            summ += i
        freq[i] = 1

    return (summ)
