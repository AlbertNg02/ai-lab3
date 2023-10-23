from .board import Board
from .utils import *
from decimal import *

from .utils import generate_one_manhattan_away

getcontext().prec = 8

class S:
    def __init__(self, board: Board):
        self.board = board
        self.probability_array = [[0 for x in range(self.board.c)] for y in range(self.board.r)]


    def get_probability(self):
        print()
        elements = Decimal(self.board.board_size())
        # location_prob = Decimal(1) / elements
        for r in range(self.board.r):
            for c in range(self.board.c):
                # self.probability_array[r][c] = location_prob
                correct = (r,c,0.6)
                print("Current Location: ({}, {})".format(r, c))
                print("    Sound reported at ({}, {}), prob: {}".format(correct[0], correct[1], correct[2]))
                possible_one_move_list = generate_one_manhattan_away(r, c, self.board)
                possible_two_move_list = generate_two_manhattan_away(r, c, self.board)
                for possible_move in possible_one_move_list:
                    print("    Sound reported at {}, prob: {} ".format(possible_move, Decimal(0.3)/Decimal(len(possible_one_move_list))))
                for possible_move in possible_two_move_list:
                    print("    Sound reported at {}, prob: {} ".format(possible_move, Decimal(0.1)/Decimal(len(possible_two_move_list))))


