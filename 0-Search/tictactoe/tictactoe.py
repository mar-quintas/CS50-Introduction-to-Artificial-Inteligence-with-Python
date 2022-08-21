"""
Tic Tac Toe Player
"""

import math
from collections import Counter
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = dict(Counter(x for xs in board for x in set(xs)))
    if board == initial_state():
        return X
    elif count["EMPTY"] == 0:
        return
    else:
        if count["X"] == count["O"]:
            return X
        else:
            return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if player(board) is None:
        return
    else:
        actions = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] is EMPTY:
                    actions.add((i, j))


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)

    if action not in actions(board):
        raise ValueError

    player_id = player(board)
    new_board[action[0]][action[1]] = player_id

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    inverted = [[], [], []]
    diagonals = [[], []]

    for i in range(len(board)):
        for j in range(len(board)):
            if j == 0:
                inverted[0].append(board[i][j])
            if j == 1:
                inverted[1].append(board[i][j])
            if j == 2:
                inverted[2].append(board[i][j])
            if j == i:
                diagonals[0].append(board[i][j])
            if (i == 2 and j == 0) or (
                    i == 1 and j == 1) or (i == 0 and j == 2):
                diagonals[1].append(board[i][j])

    rows = []
    for list in inverted:
        rows.append(list)
    for list in diagonals:
        rows.append(list)
    for list in board:
        rows.append(list)

    return winner_from_rows(rows, board)


def winner_from_rows(rows, board):
    x_winns = False
    o_winns = False

    for i in range(len(rows)):
        counter = dict(Counter(rows[i]))
        if counter.get(X, 0) == len(board):
            x_winns = True
            break
        if counter.get(O, 0) == len(board):
            o_winns = True
            break

    if x_winns:
        return X
    if o_winns:
        return O
    return


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if player(board) is None:
        return True
    if winner(board) is not None:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)

    if winner_player == X:
        return 1
    if winner_player == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
