import pip
import os
import seaborn as sns
import pandas as pd
import numpy as np
from Classes import *
from decimal import *
getcontext().prec = 8


def generate_one_manhattan_away(r, c, board):
    max_rows = board.r
    max_cols = board.c
    possible_locations = []

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_r, new_c = r + dr, c + dc
        if 0 <= new_r < max_rows and 0 <= new_c < max_cols:
            possible_locations.append((new_r, new_c))

    return possible_locations


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



def clear_heatmap_folder():
    # Get the root directory of your project
    root_directory = os.path.dirname(__file__)

    # Create the output folder path relative to the project's root
    output_folder = os.path.join(root_directory, 'heatmaps')

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    print("OUTPUTFOLDER IS ", output_folder)

    # Delete all files in the output folder
    for filename in os.listdir(output_folder):
        file_path = os.path.join(output_folder, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)



def generate_heat_map(filename, grid, time_step):
    grid = [[float(val) for val in row] for row in grid]
    df = pd.DataFrame(grid)
    p = sns.heatmap(df).set_title("Bayes Net prediction of monkey's location")

    # Get the root directory of your project
    root_directory = os.path.dirname(__file__)

    # Create the output folder path relative to the project's root
    output_folder = os.path.join(root_directory, 'heatmaps')

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Save the heatmap in the correct folder
    file_path = os.path.join(output_folder, "heatmap_timestep_{}_file_{}.png".format(time_step, filename))
    p.get_figure().savefig(file_path)
    p.get_figure().clf()

