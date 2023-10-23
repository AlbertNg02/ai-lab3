from Classes import *
from debug import *


def read_sensor_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Extract grid size from the first line
    grid_size = lines[0].split()
    m, n = int(grid_size[0]), int(grid_size[1])

    # Initialize an empty grid
    board = Board(m,n)
    debug_start(board)

    # Process sensor data from subsequent lines
    for i in range(1, len(lines)):
        data = lines[i].split()
        timestep = i - 1
        # m1, m2, sound, x, y = map(int, data)

        # Update the grid based on sensor readings
        # grid[x][y] = (m1, m2, sound)


    return 0

if __name__ == "__main__":
    # filename = input("Enter the filename: ")
    filename = "m2-input.txt"
    grid = read_sensor_data(filename)
