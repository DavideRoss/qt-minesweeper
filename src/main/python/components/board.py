from PySide2.QtWidgets import *
from PySide2.QtCore import *
from random import randrange

from settings import *
from components import Cell
from utils import Vector2

class Board():

    def __init__(self, ctx, game_layout, size):
        self.ctx = ctx
        self.game_layout = game_layout
        self.size = size

        self.layout = QGridLayout()
        self.layout.setHorizontalSpacing(0)
        self.layout.setVerticalSpacing(0)

        self.FIRST_CLICK = False
        self.create_layout()

    def create_board(self, safe_zone=None):
        # TODO: Check right size (was size.xy + 1)
        self.board = [[0 for y in range(self.size.y)] for x in range(self.size.x)]
        
        curr_mines = 0

        while curr_mines < MINES:
            x = randrange(self.size.x)
            y = randrange(self.size.y)

            if self.board[x][y] == 1:
                continue

            if safe_zone is not None and safe_zone.in_safe_zone(x, y):
                continue
            
            self.board[x][y] = 1
            curr_mines += 1

    def create_layout(self):
        self.buttons = [[0 for y in range(self.size.y)] for x in range(self.size.x)]

        for x in range(self.size.x):
            for y in range(self.size.y):
                self.buttons[x][y] = Cell(self.ctx, self)
                self.buttons[x][y].set_position(Vector2(x, y))
                self.layout.addWidget(self.buttons[x][y], x, y)

    def update_layout(self):
        for x in range(self.size.x):
            for y in range(self.size.y):
                self.buttons[x][y].update_info(self.board[x][y] == 1)

    def unload_board(self):
        for row in self.buttons:
            for b in row:
                self.layout.removeWidget(b)
                b.deleteLater()

        self.buttons = []

    def count_neighbors(self, center):
        count = 0

        neighbors = center.get_neighbors(self.size)
        for pos in neighbors:
            if self.board[pos.x][pos.y] == 1:
                count += 1

        return count

    def handle_cell_click(self, pos):
        if not self.FIRST_CLICK:
            self.FIRST_CLICK = True
            self.create_board(safe_zone=pos)
            self.update_layout()
            self.game_layout.start_timer()

        if self.board[pos.x][pos.y] == 1:
            self.game_layout.set_game_over()

            for row in self.buttons:
                for btn in row:
                    btn.set_clickable(False)

            self.show_mines()
            self.buttons[pos.x][pos.y].setStyleSheet(self.ctx.icons['ICON_MINE_RED'])
            
            return

        self.board[pos.x][pos.y] = 99
        curr_button = self.buttons[pos.x][pos.y]
        curr_button.setEnabled(False)

        if self.count_neighbors(pos) == 0:
            neighbors = pos.get_neighbors(self.size)
            curr_button.setStyleSheet(self.ctx.icons['ICON_CLICKED'])

            for n in neighbors:
                if self.board[n.x][n.y] != 99:
                    self.handle_cell_click(n)
        elif not curr_button.has_mine:
            curr_button.setStyleSheet(self.ctx.get_neighbors_style(self.count_neighbors(pos)))
        else:
            curr_button.setText('M')
    
    def edit_mine_count(self, count):
        self.game_layout.edit_mine_count(count)

    def show_mines(self):
        for x in range(self.size.x):
            for y in range(self.size.y):
                curr_button = self.buttons[x][y]

                if self.board[x][y] == 1 and not curr_button.has_flag:
                    # TODO: check for flag
                    self.buttons[x][y].setStyleSheet(self.ctx.icons['ICON_MINE'])

                if curr_button.has_flag and self.board[x][y] != 1:
                    self.buttons[x][y].setStyleSheet(self.ctx.icons['ICON_MINE_WRONG'])
