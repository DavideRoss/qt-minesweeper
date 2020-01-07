from PySide2.QtWidgets import *
from PySide2.QtCore import *

from settings import Settings
from utils import Vector2

class Cell(QPushButton):

    def __init__(self, ctx, board, parent=None):
        super(Cell, self).__init__(parent)

        self.ctx = ctx
        self.board = board

        self.setFixedSize(Settings.CELL_SIZE, Settings.CELL_SIZE)
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

    def set_temp_style(self):
        if self.has_flag:
            return

        self._tmp_style = self.styleSheet()
        self.setStyleSheet(self.ctx.icons['ICON_CLICKED'])

    def restore_temp_style(self):
        if hasattr(self, '_tmp_style'):
            self.setStyleSheet(self._tmp_style)
            del self._tmp_style

    def mousePressEvent(self, e):
        if not self.clickable:
            return
        if e.button() == Qt.LeftButton:
            self.board.set_button_style_danger()

            if not self.has_flag and not self.is_opened:
                self.setStyleSheet(self.ctx.icons['ICON_CLICKED'])
        elif e.button() == Qt.RightButton:
            if self.is_opened:
                return

            self.has_flag = not self.has_flag

            if self.has_flag:
                self.setStyleSheet(self.ctx.icons['ICON_FLAG'])
                self.board.edit_mine_count(-1)
            else:
                self.setStyleSheet(self.ctx.icons['ICON_EMPTY'])
                self.board.edit_mine_count(1)
        elif e.button() == Qt.MiddleButton:
            for p in self.position.get_neighbors(self.board.size):
                if not self.board.buttons[p.x][p.y].is_opened:
                    self.board.buttons[p.x][p.y].set_temp_style()

    def mouseReleaseEvent(self, e):
        if not self.clickable:
            return

        self.board.set_button_style_normal()
        
        if e.button() == Qt.LeftButton and not self.has_flag:
            self.board.handle_cell_click(self.position)
        elif e.button() == Qt.MidButton:
            for p in self.position.get_neighbors(self.board.size):
                self.board.buttons[p.x][p.y].restore_temp_style()

            neighbors = self.position.get_neighbors(self.board.size, include_self=True)
            flags = self.board.count_flags(neighbors)
            
            if flags == self.neighbors:
                for n in neighbors:
                    if not self.board.buttons[n.x][n.y].has_flag:
                        self.board.handle_cell_click(n)

    def set_position(self, position):
        self.position = position

    def update_info(self, has_mine):
        self.has_mine = has_mine
        self.neighbors = self.board.count_neighbors(self.position)

    def set_clickable(self, click):
        self.clickable = click
