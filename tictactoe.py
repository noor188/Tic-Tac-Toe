"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
turn  = X


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
    # X gets first move
    if board == initial_state():        
        return turn
    # Players alternate with each additional move
    turn = X if turn == O else O
    return turn

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    result = set()
    for row in range(len(board)):
        for col in range(len(board[0])):
            cellPos = (row, col)
            cellVal = board[row][col]
            if cellVal == EMPTY:
                result.add(cellPos)
    return result

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # create a deep copy
    currentBoard = copy.deepcopy(board)

    # check if action is valid
    (i, j) = action
    rows = len(board)
    cols = len(board[0])
    i_inbound = 0 <= i < rows
    j_inbound = 0 <= j < cols

    if not i_inbound or not j_inbound:
        raise IndexError(f"Invalid action: indicies ({i},{j}) are out of bounds for a board with dimensions {rows} X {cols}.")

    # Create new baord state and return board
    currentBoard[i][j] = turn
    return currentBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """    
    winner = None

    # find the winner
    # search for X
    if is_winner(board, "X"):
        winner = "X"
    # search for O
    elif is_winner(board, "O"):
        winner = "O"
    
    # winner = None , for tie or game in progress
    return winner

def is_winner(board, player):
    win_moves = {
        "horizontally" : [[(0,0), (0,1), (0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)]],
        "vertically"   : [[(0,0), (1,0), (2,0)], [(0,1), (1,1), (2,1)], [(0,2), (1,2), (2,2)]],
        "diagonally"   : [[(0,0), (1,1), (2,2)], [(0,2), (1,1), (2,0)]]
    }

    for moves in win_moves:
        for move in moves:
            x0,y0 = move[0]
            x1,y1 = move[1]
            x2,y2 = move[2]
            if board[x0][y0] == player and board[x1][y1] == player and board[x2][y2] == player:
                return True
    return False

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Game over if there is a winner or if all cells are filled
    is_there_a_winner = winner(board)
    is_all_cells_filled = all(cell is not EMPTY for row in board for cell in row)
    if is_there_a_winner or is_all_cells_filled: 
        return True 
    
    # Game in progress
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

