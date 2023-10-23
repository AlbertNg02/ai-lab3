class Board:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.board = [[0 for _ in range(r)] for _ in range(c)]

    def board_size(self):
        elements = self.r * self.c
        return elements

    def print_grid(self):
        for row in self.board:
            print(" ".join(map(str, row)))
