from .board import Board
from .utils import *
from decimal import *
getcontext().prec = 8

class M:
    def __init__(self, board: Board):
        self.board = board
        self.probability_array = [[0 for x in range(self.board.c)] for y in range(self.board.r)]




    def get_probability_M1(self, r, c):
        prob = 0.05

        if r == 0 and c == 0:
            prob = 0.9
        elif r == 0:
            prob = 0.9 - (0.1 * c)
        elif c == 0:
            prob = 0.9 - (0.1 * r)

        return max(0.05, prob)

    def get_probability_M2(self, r, c):
        prob = 0.05
        if r == (self.board.r-1) and c == (self.board.c-1):
            prob = 0.9
        if r == (self.board.r-1):
            distance = self.board.c - c - 1
            prob = 0.9 - (0.1 * distance)
        elif c == (self.board.c-1):
            distance = self.board.r - r - 1
            prob = 0.9 - (0.1 * distance)

        return max(0.05, prob)

    def print_probability(self, probs: list, monitor_number):
        print("\nMotion sensor {} distribution".format(monitor_number))
        for prob in probs:
            print("Current location {}, true prob: {}, false prob: {} ".format( prob["loc"], prob["prob"], Decimal(1) - Decimal(prob["prob"])))





    def get_probability(self):
        elements = Decimal(self.board.board_size())
        M1_probs = []
        M2_probs = []
        # location_prob = Decimal(1) / elements
        for r in range(self.board.r):
            for c in range(self.board.c):
                # self.probability_array[r][c] = location_prob
                M1_probs.append({"prob":self.get_probability_M1(r, c), "loc": (r,c)})
                M2_probs.append({"prob":self.get_probability_M2(r, c), "loc": (r,c)})

        print(self.print_probability(M1_probs, "#1 (top left)"))
        print(self.print_probability(M2_probs, "#2 (bottom right)"))


