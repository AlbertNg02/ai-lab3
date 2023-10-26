from Classes import *

from decimal import *
getcontext().prec = 8


def read_sensor_data(filename, debug: bool):
    debug_logs = debug
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Extract grid size from the first line
    grid_size = lines[0].split()

    # Initialize an empty grid
    board = Board(int(grid_size[0]), int(grid_size[1]))

    l_main = L(board)
    l_main.generate_CPT(debug)

    c_main = C(board)
    c_main.generate_CPT(debug)

    m_main = M(board)
    m_main.generate_CPT(debug)

    s_main = S(board)
    s_main.generate_CPT(debug)

    print("\nInitial distribution of monkey's last location")
    board.print_board()

    # Process sensor data from subsequent lines
    for i in range(1, len(lines)):
        time_step = i - 1
        data = lines[i].split()
        m1, m2, sound_r, sound_c = map(int, data)
        m1 = bool(m1)
        m2 = bool(m2)
        for r in range(board.r):
            for c in range(board.c):
                total_sum = calculate_prob_c_given_m1_m2_s(l_main, c_main, m_main,s_main, r, c, m1, m2, sound_r, sound_c,
                                           board)
                board.grid[r][c] = total_sum

        if debug or debug_logs:
            print("Observation: Motion1: {}, Motion2: {}, Sound Location({}, {})".format(m1, m2, sound_r, sound_c))
            print("Monkey's predicted current location at time step: {}".format(time_step))
            for rc in range(board.r):
                for cc in range(board.c):
                    print("Calculating total prob for current location ({}, {})".format(rc, cc))
                    for rl in range(board.r):
                        for cl in range(board.c):
                            print("    Probs being multiplied for last location: ({}, {}): {} {} {} {} {}".format(rl, cl, l_main.get_single_prob(rl,cl), c_main.get_single_prob(rl,cl,rc,cc), m_main.get_single_prob_m1(rc,cc,m1), m_main.get_single_prob_m2(rc,cc,m2),s_main.get_single_prob(sound_r,sound_c,rc,cc)))

            board.print_board()


        board.grid_normalised()
        print("---------------------------------------")
        debug = 0
        # print(board.grid)

        # Copy C to L
        l_main.CPT = utils.new_L_CPT(board)






    return 0


if __name__ == "__main__":
    # filename = input("Enter the filename: ")
    # debug = int(input("Enter debug boolean: 0 or 1"))
    debug = bool(int(input("Debug: 0 or 1 ")))
    filename = "m2-input.txt"
    grid = read_sensor_data(filename, debug)
