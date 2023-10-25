from .board import *
from decimal import *
from Classes import *
from .utils import *



getcontext().prec = 8

class S:
    def __init__(self, board: Board):
        self.board = board
        self.CPT = {}


    def generate_CPT(self, debug):
        print()
        for r in range(self.board.r):
            for c in range(self.board.c):
                # correct = (r,c,0.6)
                self.CPT[(r,c,r,c)] = 0.6

                if debug:
                    print("Current Location: ({}, {})".format(r, c))

                # print("    Sound reported at ({}, {}), prob: {}".format(correct[0], correct[1], self.CPT[(r,c,r,c)]))
                possible_one_move_list = generate_one_manhattan_away(r, c, self.board)
                possible_two_move_list = generate_two_manhattan_away(r, c, self.board)

                for possible_move in possible_one_move_list:
                    prob = Decimal(0.3) / Decimal(len(possible_one_move_list))
                    if debug:
                        print("    Sound reported at {}, prob: {} ".format(possible_move, prob))
                    self.CPT[(possible_move[0], possible_move[1], r, c)] = prob
                for possible_move in possible_two_move_list:
                    prob = Decimal(0.1) / Decimal(len(possible_two_move_list))
                    if debug:
                        print("    Sound reported at {}, prob: {} ".format(possible_move, prob))
                    self.CPT[(possible_move[0], possible_move[1], r, c)] = prob

    def get_single_prob(self, sr, sc, cr, cc):
        return self.CPT[(sr, sc, cr, cc)]



