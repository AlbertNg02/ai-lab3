from .board import Board
from .utils import generate_one_manhattan_away
from .utils import generate_two_manhattan_away
from decimal import *

getcontext().prec = 8


class C:
    def __init__(self, board: Board):
        """
        CPT (dict): A dictionary to store Conditional Probability Tables (CPT) with keys having 4 elements
        being L(r,c) C(r,c) and the value be P(C | L)
        """
        self.board = board
        self.CPT = {}

    def generate_CPT(self, debug):
        print()
        for r in range(self.board.r):
            for c in range(self.board.c):
                possible_move_list = generate_one_manhattan_away(r, c, self.board)
                location_prob = Decimal(1) / Decimal(len(possible_move_list))
                if debug:
                    print("Last location: ({}, {})".format(r, c))
                for possible_move in possible_move_list:
                    if debug:
                        print("    Current location {}, prob: {} ".format(possible_move, location_prob))
                    self.CPT[(r, c, possible_move[0], possible_move[1])] = location_prob

    def get_single_prob(self, lr, lc, cr, cc):
        return Decimal(self.CPT[(lr, lc, cr, cc)])
