from .board import Board
from .utils import *
from decimal import *
getcontext().prec = 8

class C:
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
                possible_move_list = generate_one_manhattan_away(r, c, self.board)
                location_prob = Decimal(1) / Decimal(len(possible_move_list))
                print("Last location: ({}, {})".format(r, c))
                for possible_move in possible_move_list:
                    print("    Current location {}, prob: {} ".format(possible_move, location_prob))


