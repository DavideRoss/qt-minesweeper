from PySide2.QtWidgets import *
from PySide2.QtCore import *
from random import randrange

from settings import *
from classes.cell import Cell

class Board():

    def __init__(self, w, h):
        self.size = size
        self.FIRST_CLICK = False

        self.create_layout()

    def create_board(self, safe_zone=None):
        self.board = [[0 for y in range(self.size.y)] for x in range(self.size.x)]
        
        curr_mines = 0

        while curr_mines <= MINES:
            x = randrange(self.size.x)
            y = randrange(self.size.y)
            
            if self.board[x][y] == 0:
                self.board[x][y] = 1
                curr_mines += 1

    # def in_safe_zone(x, y, center_x, center_y):


    def create_layout(self):
        self.buttons = [[0 for y in range(self.size.y)] for x in range(self.size.x)]

        self.layout = QGridLayout()
        self.layout.setHorizontalSpacing(0)
        self.layout.setVerticalSpacing(0)

        for x in range(self.width):
            for y in range(self.height):
                self.buttons[x][y] = Cell(self)
                # TODO: change to vector
                self.buttons[x][y].set_position(x, y)
                self.layout.addWidget(self.buttons[x][y], x, y)

    def update_layout(self):
        for x in range(self.width):
            for y in range(self.height):
                self.buttons[x][y].update_info(self.get(x, y) == 1)

    # TODO: remove
    def get(self, x, y):
        return self.board[x][y]

    # TODO: use vector2 as param
    def count_neighbors(self, center):
        count = 0

        neighbors = center.get_neighbor()

        # TODO: convert to oneline
        for pos in neighbors:
            if self.board(pos.x, pos.y) == 1:
                count += 1

        # for x in range(center.x - 1, center.x + 2):
        #     for y in range(center.y - 1, center.y + 2):
        #         if self.check_inbound(x, y) and self.board[x][y] == 1:
        #             count += 1

        return count

    # TODO: use vector2 as param
    def handle_cell_click(self, btn_x, btn_y):
        if not self.FIRST_CLICK:
            self.FIRST_CLICK = True
            self.create_board()
            self.update_layout()

        self.board[btn_x][btn_y] = 99
        self.buttons[btn_x][btn_y].setEnabled(False)

        if self.count_neighbors(btn_x, btn_y) == 0:
            for x in range(btn_x - 1, btn_x + 2):
                for y in range(btn_y - 1, btn_y + 2):
                    if self.check_inbound(x, y) and self.board[x][y] != 99:
                        self.handle_cell_click(x, y)
        elif not self.buttons[btn_x][btn_y].has_mine:
            self.buttons[btn_x][btn_y].setText(str(self.count_neighbors(btn_x, btn_y)))
        else:
            self.buttons[btn_x][btn_y].setText('M')

    def check_inbound(self, x, y):
        return x >= 0 and y >= 0 and x < self.width and y < self.height