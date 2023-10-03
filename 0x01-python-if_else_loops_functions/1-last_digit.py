#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number % 10
if number < 0 and n > 0:
    n = -10 + n
print(f"Last digit of {number:d} is {n:d} and is", end= " ")
if n == 0:
    print("0")
elif n < 6:
    print("less than 6 and not 0")
else:
    print("greater than 5")
