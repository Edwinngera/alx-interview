#!/usr/bin/python3
"""0x1F. Pascal's Triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers
       representing the Pascal’s triangle of n"""
    pascal = []
    if n <= 0:
        return pascal
    previous_row = [1]
    for row_number in range(n):
        row = []
        if row_number == 0:
            row = [1]
        else:
            for i in range(row_number + 1):
                if i == 0:
                    row.append(0 + previous_row[i])
                elif i == (row_number):
                    row.append(previous_row[i - 1] + 0)
                else:
                    row.append(previous_row[i - 1] + previous_row[i])
        previous_row = row
        pascal.append(row)
    return pascal