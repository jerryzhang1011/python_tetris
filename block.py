from colors import Color
import pygame
from pos import Pos

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.r_offset = 0
        self.c_offset = 0
        self.rotation_state = 0
        self.colors = Color.get_cell_colors()
        self.move(0, 3)
    
    def move(self, rows, colums):
        self.r_offset += rows
        self.c_offset += colums
    
    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == 4:
            self.rotation_state = 0
    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = 3

    def get_cell_position(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = []
        for i in tiles:
            i = Pos(i.r + self.r_offset, i.c + self.c_offset)
            moved_tiles.append(i)
        return moved_tiles

    def draw(self, screen, x, y):
        tiles = self.get_cell_position()
        for i in tiles:
            tile_rect = pygame.Rect(x + i.c * self.cell_size, 
                                    y + i.r * self.cell_size, 
                                    self.cell_size - 1, 
                                    self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)

