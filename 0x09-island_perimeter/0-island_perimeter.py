#!/usr/bin/python3
"""Define methods that check the perimeter of an island"""


def check_hor(grid, rowIdx, colIdx):
    """Assign grade to a column based on their right and left
    surrounding. 1 for land, 0 for water on each side"""
    row = grid[rowIdx]
    grade = 0
    if row[colIdx - 1] == 1 and colIdx != 0:
        grade += 1
    if colIdx < len(row) - 1:
        if row[colIdx + 1] == 1:
            grade += 1
    return grade


def check_vert(grid, rowIdx, colIdx):
    """Assign grade to a column based on it's up/down surrounding.
    Again, 1 for land and 0 for water"""
    grade = 0
    for idx in [rowIdx - 1, rowIdx + 1]:
        if idx >= len(grid):
            break
        if idx < 0:
            continue
        row = grid[idx]
        if row[colIdx] == 1:
            grade += 1
    return grade


def island_perimeter(grid):
    """Calculate the perimeter of the island by summing up inverses
    of grades of each piece of land.
    The logic is that the grade represent land-facing surface of each part
    of the island, and therefore adding their inverses in modulus 5 gives the
    water-facing size"""
    total = 0
    for row in grid:
        for col in row:
            grade = 4
            if col == 1:
                grade -= check_hor(grid, grid.index(row), row.index(col))
                grade -= check_vert(grid, grid.index(row), row.index(col))
                total += grade
    return total
