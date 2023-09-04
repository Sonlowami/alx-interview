#!/usr/bin/python3
"""Find a winner in a prime game"""


def is_prime(num):
    """Check if a number is prime"""
    for n in range(2, num // 2):
        if num % n == 0:
            return False
    return True


def remove_multiples(n, array):
    """Remove all nultiples of n in the array"""
    product = n
    multiple = 1
    while product < array[len(array) - 1]:
        if product in array:
            array.remove(product)
            multiple += 1
            product = n * multiple


def isWinner(x, nums):
    """Find a winner in the prime game"""
    wins = {0: 0, 1: 0}
    players = {0: 'Maria', 1: 'Ben'}
    current_player = 0
    game_round = 1
    while game_round <= x:
        index = game_round % len(nums)
        array = list(range(1, nums[index] + 1))
        for num in array:
            if len(array) == 0:
                break
            elif is_prime(num):
                remove_multiples(num, array)
                current_player = (current_player + 1) % 2
        winner = current_player
        wins[winner] += 1
        game_round += 1
    gc_winner = max(wins, key=lambda k: wins[k])
    return players[gc_winner]
