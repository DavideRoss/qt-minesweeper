from PySide2.QtWidgets import *
from PySide2.QtCore import *
from random import randrange

from settings import *
from classes.cell import Cell, Vector2

class Board():

    def __init__(self, size):
        self.size = size
        self.FIRST_CLICK = False

        self.create_layout()

    def create_board(self, safe_zone=None):
        self.board = [[0 for y in range(self.size.y + 1)] for x in range(self.size.x + 1)]
        
        curr_mines = 0

        while curr_mines <= MINES:
            x = randrange(self.size.x)
            y = randrange(self.size.y)

            print('{},{} = {}'.format(x, y, self.board[x][y]))

            if self.board[x][y] == 1:
                continue

            if safe_zone is not None and safe_zone.in_safe_zone(x, y):
                continue
            
            self.board[x][y] = 1
            curr_mines += 1

    def create_layout(self):
        self.buttons = [[0 for y in range(self.size.y)] for x in range(self.size.x)]

        self.layout = QGridLayout()
        self.layout.setHorizontalSpacing(0)
        self.layout.setVerticalSpacing(0)

        for x in range(self.size.x):
            for y in range(self.size.y):
                self.buttons[x][y] = Cell(self)
                self.buttons[x][y].set_position(Vector2(x, y))
                self.layout.addWidget(self.buttons[x][y], x, y)

    def update_layout(self):
        for x in range(self.size.x):
            for y in range(self.size.y):
                self.buttons[x][y].update_info(self.get(x, y) == 1)

    # TODO: remove
    def get(self, x, y):
        return self.board[x][y]

    def count_neighbors(self, center):
        count = 0

        neighbors = center.get_neighbors()

        # TODO: convert to oneline
        for pos in neighbors:
            if self.board[pos.x][pos.y] == 1:
                count += 1

        return count

    # TODO: use vector2 as param
    def handle_cell_click(self, pos):
        if not self.FIRST_CLICK:
            self.FIRST_CLICK = True
            self.create_board(safe_zone=pos)
            self.update_layout()

        self.board[pos.x][pos.y] = 99
        self.buttons[pos.x][pos.y].setEnabled(False)

        if self.count_neighbors(pos) == 0:
            neighbors = pos.get_neighbors()

            for n in neighbors:
                if self.board[n.x][n.y] != 99:
                    self.handle_cell_click(n)
        elif not self.buttons[pos.x][pos.y].has_mine:
            self.buttons[pos.x][pos.y].setText(str(self.count_neighbors(pos)))
        else:
            self.buttons[pos.x][pos.y].setText('M')

    # TODO: remove?
    def check_inbound(self, x, y):
        return x >= 0 and y >= 0 and x < self.width and y < self.height