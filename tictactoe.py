"""
Tic Tac Toe Player
"""

import math
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

    # initialize variables
    O_count = 0
    X_count = 0

    # loop through the board to get total num of O's and X's
    for row in board:
        for column in row:
            if column == O:
                O_count += 1
            elif column == X:
                X_count += 1

    # return values accordingly (as X goes first)
    if O_count == X_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # initialize set to store all possible actions
    possibleActions = set()

    # loop through the board and add every node with no value to the possibleActions set
    for row in range(len(board)):
        for column in range(3):
            if board[row][column] == EMPTY:
                possibleAction = (row, column)
                possibleActions.add(possibleAction)

    # return all possible actions
    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # initialize variables & copy inputed board to new board
    newBoard = copy.deepcopy(board)
    tempList = []

    # update newBoard with action
    for i in action:
        tempList.append(i)
    # return error message if action node is filled
    if tempList[0] < 0 or tempList[0] > 2 or tempList[1] < 0 or tempList[1] > 2:
        raise Exception("Invalid Action")
    elif board[tempList[0]][tempList[1]] != EMPTY:
        raise Exception("Invalid Action")
    else:
        newBoard[tempList[0]][tempList[1]] = player(board)

    # return the new board
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # check for matching rows
    for row in board:
        if all(element == X for element in row):
            return X
        elif all(element == O for element in row):
            return O

    # check for matching columns
    for column in range(3):
        if board[0][column] == X and board[1][column] == X and board[2][column] == X:
            return X
        elif board[0][column] == O and board[1][column] == O and board[2][column] == O:
            return O

    # check for matching diagonals
    if all(board[i][i] == X for i in range(3)) or all(board[i][2 - i] == X for i in range(3)):
        return X
    elif all(board[i][i] == O for i in range(3)) or all(board[i][2 - i] == O for i in range(3)):
        return O

    # if none of the conditions are met
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # check for winner
    if winner(board) == X or winner(board) == O:
        return True

    # check for tie
    elif winner(board) is None and len(actions(board)) == 0:
        return True

    # else game not over
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    # if X wins
    if winner(board) == X:
        return 1

    # if O wins
    if winner(board) == O:
        return -1

    # if tie
    return 0


def minimax_value(board):

    if terminal(board):
        return utility(board)

    # if ai player is X
    if player(board) == X:
        v = float('-inf')
        for action in actions(board):
            v = max(v, minimax_value(result(board, action)))
        return v

    # if ai player is O
    elif player(board) == O:
        v = float('inf')
        for action in actions(board):
            v = min(v, minimax_value(result(board, action)))
        return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # check for end of game
    if terminal(board):
        return None

    # if ai player is X
    elif player(board) == X:
        prev_action_value = float('-inf')
        bestAction = None
        for action in actions(board):
            new_action_value = max(prev_action_value, minimax_value(result(board, action)))
            if new_action_value > prev_action_value:
                prev_action_value = new_action_value
                bestAction = action
        return bestAction

    # if ai player is O
    elif player(board) == O:
        prev_action_value = float('inf')
        bestAction = None
        for action in actions(board):
            new_action_value = min(prev_action_value, minimax_value(result(board, action)))
            if new_action_value < prev_action_value:
                prev_action_value = new_action_value
                bestAction = action
        return bestAction
