import copy
class Board:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.single_cell_prob = 1/(self.r * self.c)
        self.grid = [[ self.single_cell_prob for _ in range(r)] for _ in range(c)]

    def board_size(self):
        elements = self.r * self.c
        return elements

    def print_board(self):
        print("---board---")
        for row in self.grid:
            print(" ".join(map(str, row)))
        print("")


    def grid_normalised(self):
        self.norm_grid = copy.deepcopy(self.grid)
        total_sum = sum(sum(row) for row in self.norm_grid)  # Calculate the sum of all values in the grid

        # Normalize and update the values in the grid
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.norm_grid[i][j] /= total_sum

        print("---normallized_board---")
        for row in self.norm_grid:
            print(" ".join(map(str, row)))
        self.grid = self.norm_grid


