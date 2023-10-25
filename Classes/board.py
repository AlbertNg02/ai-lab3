import copy
class Board:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.grid = [[0 for _ in range(r)] for _ in range(c)]

    def board_size(self):
        elements = self.r * self.c
        return elements

    def print_grid(self):
        print("\n---grid---")
        for row in self.grid:
            print(" ".join(map(str, row)))

    def print_grid_normalised(self):
        self.norm_board = copy.deepcopy(self.grid)
        total_sum = sum(sum(row) for row in self.norm_board)  # Calculate the sum of all values in the grid

        # Normalize and update the values in the grid
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.norm_board[i][j] /= total_sum

        print("\n---normallized_board---")
        for row in self.norm_board:
            print(" ".join(map(str, row)))
        # self.grid = self.norm_board

    def board_clear(self):
        self.grid = [[0 for _ in range(self.r)] for _ in range(self.c)]

