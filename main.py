from Classes import *

from debug import *
from decimal import *
getcontext().prec = 8


def read_sensor_data(filename, debug: bool):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Extract grid size from the first line
    grid_size = lines[0].split()
    board_r, board_c = int(grid_size[0]), int(grid_size[1])

    # Initialize an empty grid
    board = Board(board_r, board_c)
    # grid.print_grid()
    if debug:
        debug_start(board)

    L_CPT = L(board)
    L_CPT.generate_CPT(debug)
    C_CPT = C(board)
    C_CPT.generate_CPT(debug)
    M_CPT = M(board)
    M_CPT.generate_CPT(debug)
    S_CPT = S(board)
    S_CPT.generate_CPT(debug)

    # Process sensor data from subsequent lines
    for i in range(1, len(lines)):
        data = lines[i].split()
        m1, m2, sound_r, sound_c = map(int, data)
        for r in range(board_r):
            for c in range(board_c):
                P_l = L_CPT.get_single_prob(0, 0)
                total_sum = 0
                # total_sum = calculate_prob_c_given_m1_m2_s(L_CPT, C_CPT, M_CPT, S_CPT, r, c, m1, m2, sound_r, sound_c,
                #                                            board)
                for L_cords in utils.generate_one_manhattan_away(r, c, board):
                    p_c_given_l = C_CPT.get_single_prob(L_cords[0], L_cords[1], r, c)
                    p_m1_given_c = Decimal(M_CPT.get_single_prob_m1(r, c, m1))
                    p_m2_given_c = Decimal(M_CPT.get_single_prob_m2(r, c, m2))
                    p_s_given_c = Decimal(S_CPT.get_single_prob(sound_r, sound_c, r, c))
                    partial_sum = P_l * p_c_given_l * p_m1_given_c * p_m2_given_c * p_s_given_c
                    total_sum += partial_sum

                total_sum = total_sum
                board.grid[r][c] = total_sum

        if debug:
            board.print_grid()
        board.print_grid_normalised()

        # TODO: Enabling this breaks the code
        # L_CPT.CPT = C_CPT.CPT

        # TODO: Use new L co compute C
        # C_CPT = C(grid)
        # C_CPT.get_CPT(debug)

        # TODO: Unsure of whether we need this or not
        # board.board_clear()



    return 0


if __name__ == "__main__":
    # filename = input("Enter the filename: ")
    # debug = int(input("Enter debug boolean: 0 or 1"))
    debug = bool(False)
    filename = "m1-input.txt"
    grid = read_sensor_data(filename, debug)
