#!/usr/bin/python3
"""Contain a function minOperations that finds a the minimum number of
operations needed to fill a file with a certain number of H letters"""


def minOperations(n: int) -> int:
    """Calculate minimum number of operations to fill a file with letters
    """
    if not isinstance(n, int):
        return 0
    value = 1
    paste_value = value
    steps = 0

    while value < n:
        if n % value == 0:
            paste_value = value
            value += paste_value
            steps += 2
        else:
            value += paste_value
            steps += 1
    return steps
