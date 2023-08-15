#!/usr/bin/python3
"""Contain a function that rotates a 2D matrix"""


def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix"""
    new_matrix = []
    row, col = len(matrix) - 1, 0
    while col < len(matrix):
        new_matrix.append([])
        while row >= 0:
            new_matrix[col].append(matrix[row][col])
            row -= 1
        col += 1
        row = len(matrix) - 1
    matrix.clear()
    matrix.extend(new_matrix)
