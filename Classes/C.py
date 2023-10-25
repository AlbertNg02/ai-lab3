from .board import Board
from .utils import generate_one_manhattan_away
from .utils import generate_two_manhattan_away
from decimal import *

getcontext().prec = 8


class C:
    def __init__(self, board: Board, ):
        """
        CPT (dict): A dictionary to store Conditional Probability Tables (CPT) with keys having 4 elements
        being L(r,c) C(r,c) and the value be P(C | L)
        """
        self.board = board
        self.CPT = {}

    def generate_CPT(self, debug):
        print()
        if debug:
            print("Current location distribution:")


        # TODO: only works for first iteration
        for r in range(self.board.r):
            for c in range(self.board.c):
                self.CPT[(r,c,r,c)] = 0
                possible_move_list = generate_one_manhattan_away(r, c, self.board)

                # TODO: Question the logic
                location_prob = Decimal(1) / Decimal(len(possible_move_list))

                if debug:
                    print("Last location: ({}, {})".format(r, c))
                for possible_move in possible_move_list:
                    if debug:
                        print("    Current location {}, prob: {} ".format(possible_move, location_prob))
                    self.CPT[(r, c, possible_move[0], possible_move[1])] = location_prob

                for rr in range(self.board.r):
                    for cc in range(self.board.c):
                        if (r,c,rr,cc) not in self.CPT:
                            self.CPT[(r,c,rr,cc)] = 0


    def get_single_prob(self, rl, cl, rc, cc):
        return Decimal(self.CPT[(rl, cl, rc, cc)])



