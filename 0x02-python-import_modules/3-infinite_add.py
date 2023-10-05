#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    n = len(sys.argv)
    summ = 0

    for i in range(1, n):
        summ += int(sys.argv[i])

    print(summ)
