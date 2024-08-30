from cmath import inf

class Node:
    def __init__(self, board, move, v):
        self.board = board
        self.move = move
        self.v = v