from PySide2.QtWidgets import *
from PySide2.QtCore import *

from settings import *
from utils import Vector2
# import res

class Cell(QPushButton):

    def __init__(self, ctx, board, parent=None):
        super(Cell, self).__init__(parent)

        self.ctx = ctx
        self.board = board

        self.setFixedSize(CELL_SIZE, CELL_SIZE)
        self.setIconSize(QSize(CELL_SIZE, CELL_SIZE))

        self.setStyleSheet(self.ctx.icons['ICON_EMPTY'])

        self.is_opened = False
        self.has_flag = False
        self.has_mine = False
        self.clickable = True
        self.neighbors = 0

    def __str__(self):
        return '({}, {})'.format(str(self.position.x), str(self.position.y))

    def __repr__(self):
        return str(self)

    def mouseReleaseEvent(self, e):
        if not self.clickable:
            return
        
        # TODO: still show button on left click with flag
        if e.button() == Qt.LeftButton and not self.has_flag:
            self.board.handle_cell_click(self.position)
        elif e.button() == Qt.RightButton:
            self.has_flag = not self.has_flag

            if self.has_flag:
                self.setStyleSheet(self.ctx.icons['ICON_FLAG'])
                self.board.edit_mine_count(-1)
            else:
                self.setStyleSheet(self.ctx.icons['ICON_EMPTY'])
                self.board.edit_mine_count(1)

        elif e.button() == Qt.MidButton:
            print('Prop')

    def set_position(self, position):
        self.position = position

    def update_info(self, has_mine):
        self.has_mine = has_mine
        
        self.neighbors = self.board.count_neighbors(self.position)
        self.setEnabled(True)

    def set_clickable(self, click):
        self.clickable = click
