#!/usr/bin/python3
"""Contain method makeChange and backtrack to find smallest number
of coins needed to make a change
"""

count = -1


def makeChange(coins, total):
    """Find the smallest number of coins to make up total"""
    global count
    if total == 0:
        return 0
    if type(coins) is not list:
        return -1
    if len(coins) == 0 or (len(coins) == 1 and coins[0] != total):
        return -1
    if len(coins) == 1 and coins[0] == total:
        return 1
    for index in range(len(coins) - 1):
        backtrack(coins[index], coins[index + 1:], total, 0)
    return count


def backtrack(sam, coins, total, steps):
    """Create a backtrack to find the count of coins needed"""
    global count
    new_sam = sam + coins[0]
    if new_sam == total:
        if count != -1 and steps < count:
            count = steps + 1
    elif new_sam != total and len(coins) == 1:
        return
    if new_sam < total:
        for idx in range(len(coins) - 1):
            backtrack(new_sam, coins[idx + 1:], total, steps + 1)
