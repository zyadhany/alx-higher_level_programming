#!/usr/bin/python3
def print_last_digit(number):
    n = number % 10
    if number < 0 and n > 0:
        n = -10 + n
    return (n)
