#!/usr/bin/python3
"""
Solves the N Queens puzzle for NxN chessboard
finds placement of N number of non-attacking queens
"""

import sys


def board_set_up(N):
    """
    Sets up blank NxN chessboard

    parameters:
        N [int]: represents the size of the board

    board is initialized to 0s
    """
    matrix = []
    for row in range(N):
        matrix_row = []
        for column in range(N):
            matrix_row.append(0)
        matrix.append(matrix_row)
    return (matrix)


def print_solution(matrix):
    """
    Prints the coordinates where there is a queen

    parameters:
        matrix [list of lists]: represents the NxN chessboard

    queens indicated by 1 in matrix
    coordinates printed as list of lists
    """
    queens_coordinates = []
    for i, row in enumerate(matrix):
        for j, column in enumerate(row):
            if column == 1:
                queen = []
                queen.append(i)
                queen.append(j)
                queens_coordinates.append(queen)
    print(queens_coordinates)


def is_safe(matrix, new_row, new_column):
    """
    Determines if a queen is safe to be put in new_row, new_column

    parameters:
        matrix [list of lists]: represents the NxN chessboard
        new_row [int]: row coordinate for potential new queen
        new_column [int]: column coordinate for potential new queen
    """
    # checks row up to column (left side of row)
    for i in range(new_column):
        if matrix[new_row][i]:
            return False
    # checks upper diagonal
    for i, j in zip(range(new_row, -1, -1),
                    range(new_column, -1, -1)):
        if matrix[i][j]:
            return False
    N = len(matrix)
    # checks lower diagonal
    for i, j in zip(range(new_row, N, 1),
                    range(new_column, -1, -1)):
        if matrix[i][j]:
            return False
    return True


def solve(matrix, new_column):
    """
    Recursively solves the N Queens puzzle

    parameters:
        matrix [list of lists]: represents NxN chessboard
        new_column [int]: column to test for new queen
    """
    N = len(matrix)
    # base case: all queens are placed
    if new_column >= N:
        print_solution(matrix)
        return matrix
    for new_row in range(N):
        if is_safe(matrix, new_row, new_column):
            matrix[new_row][new_column] = 1
            # call to recursively try to solve rest of queens
            solve(matrix, new_column + 1)
            # if can't solve with this position, re-set as 0
            matrix[new_row][new_column] = 0
    return None


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    N = sys.argv[1]
    try:
        N = int(N)
    except Exception as e:
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)
    matrix = board_set_up(N)
    solve(matrix, 0)
