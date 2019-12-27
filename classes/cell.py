from PySide2.QtWidgets import *
from PySide2.QtCore import *

from settings import *
from classes import Vector2
import res

class Cell(QPushButton):

    def __init__(self, board, parent=None):
        super(Cell, self).__init__(parent)

        self.setFixedSize(CELL_SIZE, CELL_SIZE)
        self.setIconSize(QSize(CELL_SIZE, CELL_SIZE))

        self.setStyleSheet(res.styles['ICON_EMPTY'])

        self.board = board

        self.is_opened = False
        self.has_flag = False
        self.has_mine = False
        self.neighbors = 0

    def mouseReleaseEvent(self, e):
        # TODO: still show button on left click with flag
        if e.button() == Qt.LeftButton and not self.has_flag:
            self.board.handle_cell_click(self.position)
        elif e.button() == Qt.RightButton:
            self.has_flag = not self.has_flag

            if self.has_flag:
                self.setStyleSheet(res.styles['ICON_FLAG'])
                self.board.edit_mine_count(-1)
            else:
                self.setStyleSheet(res.styles['ICON_EMPTY'])
                self.board.edit_mine_count(1)

        elif e.button() == Qt.MidButton:
            print('Prop')

    # TODO: use vec2
    def set_position(self, position):
        self.position = position

    def update_info(self, has_mine):
        self.has_mine = has_mine
        
        self.neighbors = self.board.count_neighbors(self.position)
        self.setEnabled(True)

        # TODO: remove in prod
        # if self.has_mine:
        #     self.setStyleSheet(res.styles['ICON_MINE'])

        # TODO: reset icon
        # self.setText('')
        # self.setIcon(res.icons['ICON_EMPTY'])