#!/usr/bin/python3
"""
Create a function def pascal_triangle(n):
that returns a list of lists of integers representing
the Pascal's triangle of n:
Returns an empty list if n <= 0
You can assume n will be always an integer
"""


def pascal_triangle(n):
    """
    This code effectively generates
    Pascal's Triangle by iteratively
    calculating the values of each row
    based on the previous row.
    """
    if n <= 0:
        return[]

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)  # Start with a row of ones
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)

    return triangle
