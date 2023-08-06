#!/usr/bin/python3
"""Find the correct arrangement of N non-attacking queens in an NxN matrix"""
import sys

blocked_cols = set()
pos_diags = set()
neg_diags = set()
positions = []


def find_positions(row, n):
    """Find a non-attacking position for the next queen"""
    if row == n:
        print(positions)
        return
    for col in range(n):
        is_blocked = col in blocked_cols
        is_diag = (row + col) in pos_diags or (row - col) in neg_diags
        if is_blocked or is_diag:
            continue
        blocked_cols.add(col)
        pos_diags.add(row + col)
        neg_diags.add(row - col)
        positions.append([col, row])
        find_positions(row + 1, n)

        blocked_cols.remove(col)
        pos_diags.remove(row + col)
        neg_diags.remove(row - col)
        positions.remove([col, row])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        if n < 4:
            print('N must be at least 4')
            sys.exit(1)
        find_positions(0, n)
    except ValueError:
        print('N must be a number')
        sys.exit(1)
