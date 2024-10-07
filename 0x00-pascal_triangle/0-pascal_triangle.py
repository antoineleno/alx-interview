#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    """Pascall Triangle"""
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        triangle = [[1], [1, 1]]
        for i in range(2, n):
            row = []
            for j in range(len(triangle[-1])):
                try:
                    row.append(triangle[-1][j] + triangle[-1][j + 1])
                except IndexError:
                    row.insert(0, 1)
                    row.append(1)
            triangle.append(row)
        return triangle
