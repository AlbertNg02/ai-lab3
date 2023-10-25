from .board import Board
from decimal import *
getcontext().prec = 8

class L:
    def __init__(self, board: Board):
        self.board = board
        self.CPT = {}

        """
        CPT (dict): A dictionary to store Conditional Probability Tables (CPT) with keys having 2 elements
        being r, c and the value be L
        """


    def generate_CPT(self, debug):
        elements = Decimal(self.board.board_size())
        location_prob = Decimal(1) / elements
        for r in range(self.board.r):
            for c in range(self.board.c):
                self.CPT[(r,c)] = location_prob
                if debug:
                    print("Last location: ({}, {}), prob: {} ".format(r, c, location_prob))


    def get_single_prob(self, r, c):
        return self.CPT[(r,c)]

