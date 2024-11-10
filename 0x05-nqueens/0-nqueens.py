#!/usr/bin/python3

import sys


def solve(row, column):
    """
    Solve the N-Queens problem.

    Args:
        row (int): The number of rows in the board.
        column (int): The number of columns in the board.

    Returns:
        list: A list of solutions.

    """
    solver = [[]]
    for q in range(row):
        solver = place_queen(q, column, solver)
    return solver


def place_queen(q, column, prev_solver):
    """
    Place a queen in a column in a given row.

    Args:
        q (int): The row in which to place the queen.
        column (int): The column in which to place the queen.
        prev_solver (list): The list of solutions found so far.

    Returns:
        list: The list of solutions with the new queen placed.

    """
    solver_queen = []
    for array in prev_solver:
        for x in range(column):
            if is_safe(q, x, array):
                solver_queen.append(array + [x])
    return solver_queen


def is_safe(q, x, array):
    """
    Check if a queen can be placed in a given position.

    Args:
        q (int): The row in which to place the queen.
        x (int): The column in which to place the queen.
        array (list): The list of columns in which queens are already placed.

    Returns:
        bool: True if the queen can be placed, False otherwise.

    """
    if x in array:
        return False
    else:
        return all(abs(array[column] - x) != q - column
                   for column in range(q))


def init():
    """
    Initialize the program.

    Returns:
        int: The number of queens to place.

    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        the_queen = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if the_queen < 4:
        print("N must be at least 4")
        sys.exit(1)
    return the_queen


def n_queens():
    """
    Run the program.

    """
    the_queen = init()
    solver = solve(the_queen, the_queen)
    for array in solver:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)


if __name__ == '__main__':
    n_queens()
