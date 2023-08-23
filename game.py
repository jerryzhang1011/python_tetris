from grid import Grid
from Blocks import *
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.curr = self.get_random_block()
        self.next = self.get_random_block()
        self.game_over = False
        self.score = 0

    def update_score(self, clear, move_down):
        if clear == 1:
            self.score += 100
        elif clear == 2:
            self.score += 300
        elif clear == 3:
            self.score += 500
        self.score += move_down


    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        b = random.choice(self.blocks)
        self.blocks.remove(b)
        return b

    def move_left(self):
        self.curr.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.curr.move(0, 1)
    def move_right(self):
        self.curr.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.curr.move(0, -1)
    def move_down(self):
        self.curr.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.curr.move(-1, 0)
            self.lock_block()
    def lock_block(self):
        tiles = self.curr.get_cell_position()
        for i in tiles:
            self.grid.grid[i.r][i.c] = self.curr.id
        self.curr = self.next
        self.next = self.get_random_block()
        num = self.grid.clear_full_rows()
        self.update_score(num, 0)
        if self.block_fits() == False:
            self.game_over = True

    def block_fits(self):
        tiles = self.curr.get_cell_position()
        for i in tiles:
            if self.grid.is_empty(i.r, i.c) == False:
                return False
        return True

    def block_inside(self):
        tiles = self.curr.get_cell_position()
        for i in tiles:
            if self.grid.is_inside(i.r, i.c) == False:
                return False
        return True

    def draw(self, screen):
        self.grid.draw(screen)
        self.curr.draw(screen, 0, 0)
        if self.next.id == 3:
            self.next.draw(screen, 260, 280)
        elif self.next.id == 4:
            self.next.draw(screen, 255, 265)
        else:
            self.next.draw(screen, 265, 265)
    
    def rotate(self):
        self.curr.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.curr.undo_rotation()

    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.curr = self.get_random_block()
        self.next = self.get_random_block()
        self.score = 0
        