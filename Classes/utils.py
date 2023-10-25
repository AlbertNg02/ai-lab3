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
def generate_one_manhattan_away(r, c, board: Board):
    max_rows = board.r
    max_cols = board.c
    possible_locations = []

    # Check if moving up is a valid step
    if r > 0:
        possible_locations.append((r - 1, c))

    # Check if moving down is a valid step
    if r < max_rows - 1:
        possible_locations.append((r + 1, c))

    # Check if moving left is a valid step
    if c > 0:
        possible_locations.append((r, c - 1))

    # Check if moving right is a valid step
    if c < max_cols - 1:
        possible_locations.append((r, c + 1))

    return possible_locations


# TODO: Implement a function to generate a list of all possible (r, c) locations two Manhattan-steps away from a given location.
def generate_two_manhattan_away(r, c, board: Board):
    max_rows = board.r
    max_cols = board.c
    possible_locations = []

    # Check if moving up is a valid step
    if r > 1:
        possible_locations.append((r - 2, c))

    # Check if moving down is a valid step
    if r < max_rows - 2:
        possible_locations.append((r + 2, c))

    # Check if moving left is a valid step
    if c > 1:
        possible_locations.append((r, c - 2))

    # Check if moving right is a valid step
    if c < max_cols - 2:
        possible_locations.append((r, c + 2))

    # Check if moving diagonally up-left is a valid step
    if r > 0 and c > 0:
        possible_locations.append((r - 1, c - 1))

    # Check if moving diagonally up-right is a valid step
    if r > 0 and c < max_cols - 1:
        possible_locations.append((r - 1, c + 1))

    # Check if moving diagonally down-left is a valid step
    if r < max_rows - 1 and c > 0:
        possible_locations.append((r + 1, c - 1))

    # Check if moving diagonally down-right is a valid step
    if r < max_rows - 1 and c < max_cols - 1:
        possible_locations.append((r + 1, c + 1))

    return possible_locations


def calculate_prob_c_given_m1_m2_s(L_CPT, C_CPT, M_CPT, S_CPT, r, c, m1, m2, sound_r, sound_c, board):
    P_l = L_CPT.get_single_prob(0, 0)
    total_sum = 0
    for L_cords in generate_one_manhattan_away(r, c, board):
        p_c_given_l = C_CPT.get_single_prob(L_cords[0], L_cords[1], r, c)
        p_m1_given_c = Decimal(M_CPT.get_single_prob_m1(r, c, m1))
        p_m2_given_c = Decimal(M_CPT.get_single_prob_m2(r, c, m2))
        p_s_given_c = Decimal(S_CPT.get_single_prob(sound_r, sound_c, r, c))
        partial_sum = P_l * p_c_given_l * p_m1_given_c * p_m2_given_c * p_s_given_c
        total_sum += partial_sum
    return total_sum



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