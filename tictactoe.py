"""
Tic Tac Toe Player
"""

from cmath import inf
from node import Node
import math
import copy
import random

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

def count_moves(board):
    """
    Returns number of x's and o's on the board

    """
    first = second = 0

    for r in board:
        for c in r:
            if c == "X":
                first+=1
            elif c == "O":
                second+=1
    
    return first, second

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    player_moves = count_moves(board)
    
    #If board is empty or same number of x's and o's on board, it's x's turn
    if player_moves == (0,0) or player_moves[0] == player_moves[1]:
        return X
    #If max number of x's reached return "Game Over"
    elif player_moves[0] == 5:
        return "Game Over"
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    next = player(board)
    if next == "Game Over":
        return next
    
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == EMPTY:
                actions.append((r,c))
    
    return actions

def contains_action(action, actions):
    for item in actions:
        if item[0] == action[0] and item[1] == action[1]:
            return True
    return False 

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action[0] < 0 or action[0] >= len(board) or action[1] > len(board[0]) :
        raise ValueError("Out of Bounds")
    if not contains_action(action,actions(board)):
        raise ValueError("Occupied")
    
    new_board = copy.deepcopy(board)
    
    if player(board) != "Game Over":
        new_board[action[0]][action[1]] = player(board)

    return new_board

def none(items):
    for item in items:
        if item == None:
            return True
    return False

def cardinal(board):
    #Returns a tuple (true/false won, winner letter)

    #Check horizontally if the board has the same letter 3 in a row
    for r in range(len(board)):
        if not none([board[r][0], board[r][1], board[r][2]]):
            if board[r][0] == board[r][1] == board[r][2]:
                return True, board[r][0]

    #Check vertically if the board has the same letter 3 in a row
    for c in range(len(board[0])):
        if not none([board[0][c], board[1][c], board[2][c]]):
            if board[0][c] == board[1][c] == board[2][c]:
                return True, board[0][c]

    return False, None

def diagonal(board):
    #Returns a tuple (true/false won, winner letter)
 
    if board[1][1] != None:
        if board[0][0] == board[1][1] == board[2][2]:
            return True, board[0][0]
        if board[0][2] == board[1][1] == board[2][0]:
            return True, board[0][2]
    
    return False,None

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if cardinal(board)[0]:
        return cardinal(board)[1]
    if diagonal(board)[0]:
        return diagonal(board)[1]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) != None or player(board) == 'Game Over'


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)

    if win == X:
        return 1
    elif win == O:
        return -1
    return 0

def max_value(board):
    v = -inf
    act = None

    if terminal(board):
        v = utility(board)
        return v, None
    
    for action in actions(board):
        temp, move= min_value(result(board,action))
        if temp > v:
            v = temp
            act = action
        
    return v,act

def min_value(board):
    v = inf
    act = None

    if terminal(board):
        v = utility(board)
        #print(f'{board} score: {utility(board)}')
        return v, None


    for action in actions(board):
        temp, move = max_value(result(board,action))
        if temp < v:
            v = temp
            act = action

    return v,act

def boards_equal(board1,board2):
    for r in range(len(board1)):
        for c in range(len(board1[0])):
            if board1[r][c] != board2[r][c]:
                return False
    return True

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
   
    if terminal(board):
        return None
    #If player is O minimize
    if player(board) == O:
        
        if 1 == random.randint(0,5):
            moves = actions(board)
            return moves[random.randint(0,len(moves)-1)]
        
        action = min_value(board)[1]
        
        return action
            
       

    #If player is X maximize
    if player(board) == X:
        if boards_equal(board, initial_state()):
            return (random.randint(0,2),random.randint(0,2))    
        action = max_value(board)[1]
        return action
       

    return None
