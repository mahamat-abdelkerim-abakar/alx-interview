#!/usr/bin/python3
"""N Queens"""
import sys


def format_requirements(board):
    """Prints according to requirements"""
    ret = []
    for i in range(len(board)):
        colIdx = board[i].index(1)
        ret.append([i, colIdx])
    print(ret)


def is_valid_queen(board, curCol, row, n):
    """Checks if element is a valid queen"""
    # Check prev columns
    for i in range(curCol):
        if board[row][i] == 1:
            return False
    # Check for upper diagonal
    i = row
    j = curCol
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # Check for lower diagonal
    i = row
    j = curCol
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True


def nQueens(board, curCol, n):
    """Recursive call that places queens in all the
    posible positions of the board"""
    stat = False
    if curCol == n:
        format_requirements(board)
        return True
    for row in range(0, n):
        if is_valid_queen(board, curCol, row, n):
            board[row][curCol] = 1
            stat = nQueens(board, curCol + 1, n) or stat
            board[row][curCol] = 0
    return stat


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)
    board = [[0 for i in range(n)] for j in range(n)]
    # first col is 0
    nQueens(board, 0, n)
