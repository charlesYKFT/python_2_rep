"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    """Checks the board and return the result of tic_tac game"""
    if all(len(row) != len(board) for row in board) or len(board) != 3:
        raise TypeError("Incorrect board!")

    # Check rows
    for row in board:
        if all(cell == 'x' for cell in row):
            return 'x wins!'
        elif all(cell == 'o' for cell in row):
            return 'o wins!'

    # Check columns
    for col in range(len(board[0])):
        if all(row[col] == 'x' for row in board):
            return 'x wins!'
        elif all(row[col] == 'o' for row in board):
            return 'o wins!'

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'x':
            return 'x wins!'
        elif board[0][0] == 'o':
            return 'o wins!'
    elif board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'x':
            return 'x wins!'
        elif board[0][2] == 'o':
            return 'o wins!'

    # Check for unfinished board
    for row in board:
        if '-' in row:
            return 'The board is unfinished!'

    # If none of the above conditions are met, it's a draw
    return 'draw!'
