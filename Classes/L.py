from .board import Board
from decimal import *
getcontext().prec = 8

class L:
    def __init__(self, board: Board):
        self.board = board
        self.probability_array = [[0 for x in range(self.board.c)] for y in range(self.board.r)]


    def get_probability(self):
        elements = Decimal(self.board.board_size())
        location_prob = Decimal(1) / elements
        for r in range(self.board.r):
            for c in range(self.board.c):
                self.probability_array[r][c] = location_prob
                print("Last location: ({}, {}), prob: {} ".format(r, c, location_prob))



