#!/usr/bin/python3
"""Define a method"""


def pascal_traingle(n):
    """
    returns a list of integers representing
    the pascal's triangle of n

    Args:
        n: Integer
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for x in range(1, n):
        prevRow = triangle[x - 1]
        newRow = [1]

        for y in range(1, x):
            newValue = preRow[y - 1] + prevRow[y]
            newRow.append(newValue)

        newRow.append(1)
        triangle.append(newRow)

    return triangle
