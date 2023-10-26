# import seaborn as sns
# import pandas as pd
# import numpy as np
from Classes import *
from decimal import *
getcontext().prec = 8

# TODO: Create a function to generate a list of all possible (r, c) locations on the grid.
def generate_all_locations(board: Board):
    # m, n = grid.board_size()
    pass


# TODO: Develop a function to generate a list of all possible (r, c) locations one Manhattan-step away from a given location.
def generate_one_manhattan_away(r, c, board):
    max_rows = board.r
    max_cols = board.c
    possible_locations = []

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_r, new_c = r + dr, c + dc
        if 0 <= new_r < max_rows and 0 <= new_c < max_cols:
            possible_locations.append((new_r, new_c))

    return possible_locations


# TODO: Implement a function to generate a list of all possible (r, c) locations two Manhattan-steps away from a given location.
def generate_two_manhattan_away(r, c, board: Board):
    max_rows = board.r
    max_cols = board.c
    possible_locations = []

    # Check if moving two steps up is a valid step
    directions = [(2, 0), (-2, 0), (0, 2), (0, -2), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    for dr, dc in directions:
        new_r, new_c = r + dr, c + dc
        if 0 <= new_r < max_rows and 0 <= new_c < max_cols:
            possible_locations.append((new_r, new_c))

    return possible_locations


def calculate_prob_c_given_m1_m2_s(L_CPT, C_CPT, M_CPT, S_CPT, r, c, m1, m2, sound_r, sound_c, board):

    # TODO: Albert you should have never used this EVER EVER EVER
    total_sum = 0
    for L_cords in generate_one_manhattan_away(r, c, board):
        p_l = L_CPT.get_single_prob(L_cords[0], L_cords[1])
        p_c_given_l = C_CPT.get_single_prob(L_cords[0], L_cords[1], r, c)
        p_m1_given_c = Decimal(M_CPT.get_single_prob_m1(r, c, m1))
        p_m2_given_c = Decimal(M_CPT.get_single_prob_m2(r, c, m2))
        p_s_given_c = Decimal(S_CPT.get_single_prob(sound_r, sound_c, r, c))
        partial_sum = p_l * p_c_given_l * p_m1_given_c * p_m2_given_c * p_s_given_c
        total_sum += partial_sum
    return total_sum



def new_L_CPT(board: Board):

    new_L_CPT = {}

    for r in range(board.r):
        for c in range(board.c):
            new_L_CPT[(r,c)] = board.grid[r][c]
    print("")

    return new_L_CPT



# def generate_heat_map(grid):
#     # Create a dataset
#     df = pd.DataFrame(np.random.random((5, 5)), columns=["a", "b", "c", "d", "e"])
#
#     # Default heatmap
#     p1 = sns.heatmap(df)
#     p1
#     p1.get_figure().savefig("heatmap.png")
#
# generate_heat_map(0)