#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    n = len(my_list)

    if idx < 0 or idx >= n:
        return my_list
    X = my_list[0:idx] + my_list[idx + 1:]
    return (X)
