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

    unlocked = {0}
    keys_available = boxes[0]
    while keys_available:
        key = keys_available.pop(0)
        if key < len(boxes) and key not in unlocked:
            unlocked.add(key)
            keys_available.extend(boxes[key])

    return True if (len(unlocked) == len(boxes)) else False
