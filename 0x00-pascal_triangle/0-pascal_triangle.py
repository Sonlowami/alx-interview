#!/usr/bin/python3
"""This file containa  function that emulates a pascal's triangle
of size n"""


def pascal_triangle(n):
    """Return a list representing rows of a pascal's triangle"""
    triangle_list = []
    if n <= 0:
        return triangle_list
    i = 0
    while i < n:
        row = []
        j = 1
        if i - 1 >= 0:
            while j <= i:
                if j >= 2:
                    row.append(triangle_list[i-1][j-1] +
                               triangle_list[i-1][j-2])
                else:
                    row.append(1)
                j += 1
        row.append(1)
        triangle_list.append(row)
        i += 1
    return triangle_list
