from .board import Board
from .utils import *
from decimal import *

getcontext().prec = 8


class M:
    def __init__(self, board: Board):
        self.board = board
        self.M1_CPT = {}
        self.M2_CPT = {}

    def get_CPT_M1(self, r, c):
        prob = 0.05
        if r == 0 and c == 0:
            prob = 0.9
        elif r == 0:
            prob = 0.9 - (0.1 * c)
        elif c == 0:
            prob = 0.9 - (0.1 * r)

        return max(0.05, prob)

    def get_CPT_M2(self, r, c):
        prob = 0.05
        if r == (self.board.r - 1) and c == (self.board.c - 1):
            prob = 0.9
        elif r == (self.board.r - 1):
            distance = self.board.c - c - 1
            prob = 0.9 - (0.1 * distance)
        elif c == (self.board.c - 1):
            distance = self.board.r - r - 1
            prob = 0.9 - (0.1 * distance)

        return max(0.05, prob)

    def print_probability(self, probs: dict, monitor_number):
        print("\nMotion sensor {} distribution".format(monitor_number))
        for loc, prob in probs.items():
            print("Current location {}, true prob: {}, false prob: {} ".format(loc, prob, Decimal(1) - Decimal(prob)))

    def generate_CPT(self, debug):
        for r in range(self.board.r):
            for c in range(self.board.c):
                # TODO: Check logic first iteration should always equal to 1
                self.M1_CPT[(r, c)] = self.get_CPT_M1(r, c)
                self.M2_CPT[(r, c)] = self.get_CPT_M2(r, c)

        if debug:
            print(self.print_probability(self.M1_CPT, "#1 (top left)"))
            print(self.print_probability(self.M2_CPT, "#2 (bottom right)"))

    def get_single_prob_m1(self, r, c, m1):

        # if (r == 0 or c == 0) and m1 == True:
        #     correct_sensor = True
        # elif (r != 0 and c != 0) and m1 == False:
        #     correct_sensor = True
        # else:
        #     correct_sensor = False
        #
        # if correct_sensor:
        #     m1_true = Decimal(self.M1_CPT[(r, c)])
        #     return m1_true
        # else:
        #     m1_false = Decimal(1) - Decimal(self.M1_CPT[(r, c)])
        #     return m1_false
        if m1:
            return (Decimal(self.M1_CPT[(r,c)]))
        else:
            return 1 - (Decimal(self.M1_CPT[(r,c)]))

    def get_single_prob_m2(self, r, c, m2):
        # if (r == self.board.r - 1 or c == self.board.c - 1) and m2 == True:
        #     correct_sensor = True
        # elif (r != self.board.r - 1 and c != self.board.c - 1) and m2 == False:
        #     correct_sensor = True
        # else:
        #     correct_sensor = False
        #
        # if correct_sensor:
        #     m2_true = Decimal(self.M2_CPT[(r, c)])
        #     return m2_true
        # else:
        #     m2_false = Decimal(1) - Decimal(self.M2_CPT[(r, c)])
        #     return m2_false
        if m2:
            return (Decimal(self.M2_CPT[(r,c)]))
        else:
            return 1 - (Decimal(self.M2_CPT[(r,c)]))

