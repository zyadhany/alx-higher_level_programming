#!/usr/bin/python3
def search_replace(my_list, search, replace):
    X = []

    for i in my_list:
        if i == search:
            X.append(replace)
        else:
            X.append(i)
    return (X)
