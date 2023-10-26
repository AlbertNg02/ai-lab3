from .board import *
from decimal import *
from Classes import *
from .utils import *
from .utils import generate_one_manhattan_away
from .utils import generate_two_manhattan_away

getcontext().prec = 8

class S:
    def __init__(self, board: Board):
        self.board = board
        self.CPT = {}


    # def generate_CPT(self, debug):
    #     print()
    # self.C_CPT = C_CPT
    #     if debug:
    #         print("Sound distribution:")
    #     for rc in range(self.board.r):
    #         for cc in range(self.board.c):
    #             if debug:
    #                 print("Current Location: ({}, {})".format(rc, cc))
    #             possible_one_move_list = generate_one_manhattan_away(rc, cc, self.board)
    #             possible_two_move_list = generate_two_manhattan_away(rc, cc, self.board)
    #             self.CPT[(rc, cc, rc, cc)] = 0.6
    #             if debug:
    #                 print("    Sound reported at {}, prob: {} ".format((rc, cc), 0.6))
    #
    #             for rs in range(self.board.r):
    #                 for cs in range(self.board.c):
    #
    #                     if (rs, cs) in possible_one_move_list:
    #                         prob = Decimal(0.3) / Decimal(len(possible_one_move_list))
    #                         if debug:
    #                             print("    Sound reported at {}, prob: {} ".format((rs,cs), prob))
    #                         self.CPT[(rs, cs, rc, cc)] = prob
    #                     elif (rs, cs) in possible_two_move_list:
    #                         prob = Decimal(0.1) / Decimal(len(possible_two_move_list))
    #                         if debug:
    #                             print("    Sound reported at {}, prob: {} ".format((rs,cs), prob))
    #                         self.CPT[(rs, cs, rc, cc)] = prob
    #                     else:
    #                         self.CPT[(rs, cs, rc, cc)] = 0

    def generate_CPT(self, debug):
        print()
        if debug:
            print("Sound distribution:")
        for r in range(self.board.r):
            for c in range(self.board.c):
                self.CPT[(r, c, r, c)] = 0.6

                if debug:
                    print("Current Location: ({}, {})".format(r, c))
                    print("    Sound reported at {}, prob: {} ".format((r,c), self.CPT.get((r,c,r,c))))

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

                for rr in range(self.board.r):
                    for cc in range(self.board.c):
                        if (r,c,rr,cc) not in self.CPT:
                            self.CPT[(r,c,rr,cc)] = 0

    def get_single_prob(self, rs, cs, rc, cc):
        return self.CPT[(rs, cs, rc, cc)]



