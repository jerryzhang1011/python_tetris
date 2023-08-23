import pygame
from colors import Color
class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_col = 10
        self.cell_size = 30
        self.grid = [[0 for i in range(self.num_col)] for i in range(self.num_rows)]
        self.colors = Color.get_cell_colors()

    def print_grid(self):
        for r in range(self.num_rows):
            for c in range(self.num_col):
                print(self.grid[r][c], end=" ")
            print()
    
    def is_inside(self, r, c):
        return r >= 0 and r < self.num_rows and c >= 0 and c < self.num_col

    def is_empty(self, r, c):
        return self.grid[r][c] == 0
    
    def is_row_full(self, row):
        for i in self.grid[row]:
            if i == 0:
                return False
        return True

    def clear_row(self, row):
        for i in self.grid[row]:
            i = 0
    
    def move_row_down(self, row, num):
        for i in range(self.num_col):
            self.grid[row + num][i] = self.grid[row][i]
            self.grid[row][i] = 0

    def clear_full_rows(self):
        complete = 0
        for i in range (self.num_rows - 1, 0, -1):
            if self.is_row_full(i) == True:
                self.clear_row(i)
                complete += 1
            elif complete > 0:
                self.move_row_down(i, complete)
        return complete

    def reset(self):
        self.grid = [[0 for i in range(self.num_col)] for i in range(self.num_rows)]

    def draw(self, screen):
        for r in range(self.num_rows):
            for c in range(self.num_col):
                cell_value = self.grid[r][c]
                cell_rect = pygame.Rect(c*self.cell_size, r*self.cell_size, self.cell_size -1, self.cell_size - 1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
