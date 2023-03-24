#!/usr/bin/python3
""" Pascal's triangle"""


def pascal_triangle(n):
    """Pascal's triangle"""
    row1 = []

    if (n <= 0):
        return row1
    for i in range(1, (n + 1)):
        row2 = []
        for j in range(i):
            row2.append(1)
        row1.append(row2)
    for i in range(len(row1)):
        for j in range(i):
            if j != 0:
                row1[i][j] = row1[i - 1][j] + row1[i - 1][j - 1]
    return row1
