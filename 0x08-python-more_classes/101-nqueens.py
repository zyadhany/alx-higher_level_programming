#!/usr/bin/python3

import sys


def isposible(board=[], L=0, R=0):

    for a in board:
        if L == a[0] or R == a[1]:
            return (0)
        if abs(a[0] - L) == abs(a[1] - R):
            return (0)
    return (1)


def req(board=[], at=0, n=0, k=0):
    if n == k:
        print(board)
        return

    if at == n * n or k < at // n:
        return

    if (isposible(board, at // n, at % n)):
        board.append([at // n, at % n])
        req(board, at + 1, n, k + 1)
        board.pop()
        pass

    req(board, at + 1, n, k)
    pass


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    n = int(sys.argv[1])

    req(n=n)
