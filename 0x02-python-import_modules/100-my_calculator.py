#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, div, mul, sub
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    opp = sys.argv[2]
    
    if opp == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif opp == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif opp == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif opp == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
