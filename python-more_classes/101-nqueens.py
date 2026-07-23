#!/usr/bin/python3
"""Solves the N queens puzzle and prints every solution.

Usage:
    ./101-nqueens.py N

Where N is the size of the N x N chessboard (and the number of queens
to place so that none of them attack each other).
"""
import sys


def is_safe(board, row, col):
    """Check whether a queen can be placed at (row, col) safely.

    Args:
        board (list): board[r] holds the column of the queen already
            placed in row r, for every row before `row`.
        row (int): The row being considered for a new queen.
        col (int): The column being considered for a new queen.

    Returns:
        bool: True if no earlier queen shares this column or diagonal.
    """
    for placed_row in range(row):
        placed_col = board[placed_row]
        if placed_col == col:
            return False
        if abs(placed_col - col) == abs(placed_row - row):
            return False
    return True


def solve(size, row, board, solutions):
    """Recursively place one queen per row using backtracking.

    Args:
        size (int): The size of the board (N).
        row (int): The row currently being filled.
        board (list): board[r] holds the column of row r's queen.
        solutions (list): Accumulator for every complete solution found.
    """
    if row == size:
        solutions.append(board[:])
        return

    for col in range(size):
        if is_safe(board, row, col):
            board[row] = col
            solve(size, row + 1, board, solutions)
            board[row] = -1


def print_solution(board):
    """Print one solution as a list of [row, column] pairs.

    Args:
        board (list): board[r] holds the column of row r's queen.
    """
    print([[row, col] for row, col in enumerate(board)])


def parse_size():
    """Validate argv and return N, or exit with the required message.

    Returns:
        int: The validated board size, guaranteed to be >= 4.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    return size


if __name__ == "__main__":
    n = parse_size()
    all_solutions = []
    solve(n, 0, [-1] * n, all_solutions)
    for one_solution in all_solutions:
        print_solution(one_solution)
