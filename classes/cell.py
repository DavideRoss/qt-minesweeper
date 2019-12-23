from PySide2.QtWidgets import *
from PySide2.QtCore import *

from settings import *
from classes import Vector2

class Cell(QPushButton):

    def __init__(self, board, parent=None):
        super(Cell, self).__init__(parent)

        self.setFixedSize(CELL_SIZE, CELL_SIZE)
        self.board = board

        self.is_opened = False
        self.has_flag = False
        self.has_mine = False
        self.neighbors = 0

    def mouseReleaseEvent(self, e):
        print(e.button())
        if e.button() == Qt.LeftButton:
            self.board.handle_cell_click(self.position)
        elif e.button() == Qt.RightButton:
            print('Flag')
            self.setStyleSheet('color: #a00; font-weight: bold')
        elif e.button() == Qt.MidButton:
            print('Prop')

    # TODO: use vec2
    def set_position(self, position):
        self.position = position

    def update_info(self, has_mine):
        self.has_mine = has_mine
        
        self.neighbors = self.board.count_neighbors(self.position)
        self.setEnabled(True)
        self.setText('')

        if self.has_mine:
            self.setText('M')