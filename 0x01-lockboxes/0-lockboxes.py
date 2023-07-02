#!/usr/bin/python3
"""
This file contain a function to check whether given a list of
boxes, where each box may contain keys to other boxes, all boxes can be opened
"""


def canUnlockAll(boxes):
    """Check if all boxes can be unlocked"""

    if not isinstance(boxes, list):
        return False
    elif len(boxes) == 1:
        return True

    boxcopy = boxes[:]
    unlocked = {0}

    for keys in boxcopy:
        for key in keys:
            if key < len(boxcopy):
                unlocked.add(key)
        print(unlocked)
        print(boxcopy)
    return True if (len(unlocked) == len(boxcopy)) else False
