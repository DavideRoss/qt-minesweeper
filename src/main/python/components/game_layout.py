from PySide2.QtWidgets import *
from PySide2.QtCore import *

from components import Board
from utils import Vector2
from settings import *

class GameLayout(QVBoxLayout):

    def __init__(self, ctx, parent=None):
        super(GameLayout, self).__init__(parent)

        self.ctx = ctx
        self.init_top_ui()

    def init_top_ui(self):
        # Layout
        self.top_layout = QHBoxLayout()
        self.top_layout.setObjectName("top_layout")

        # Mines left
        self.mines_label = QLCDNumber()
        self.mines_label.setSegmentStyle(QLCDNumber.Flat)
        self.top_layout.addWidget(self.mines_label)

        # Restart button
        self.restart_btn = QPushButton()

        self.restart_btn.setFixedSize(50, 50)
        self.restart_btn.clicked.connect(self.handle_restart_button)
        self.restart_btn.pressed.connect(self.set_button_style_pressed)
        self.restart_btn.released.connect(self.set_button_style_normal)
        self.set_button_style_normal()

        self.top_layout.addWidget(self.restart_btn)

        # Clock
        self.clock_label = QLCDNumber()
        self.clock_label.setSegmentStyle(QLCDNumber.Flat)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)

        self.top_layout.addWidget(self.clock_label)
        self.addLayout(self.top_layout)

    def start_timer(self):
        self.timer.start(1000)

    def create_new_game(self, size, mines):
        if hasattr(self, 'board'):
            self.board.unload_board()
            self.removeItem(self.board.layout)

        self.game_over = False
        self.timer_counter = 0
        self.current_mines = mines
        self.timer.stop()
        
        self.board = Board(self.ctx, self, size, mines)
        self.addLayout(self.board.layout)
        self.update_top_layout()

    def update_top_layout(self):
        self.mines_label.display(self.current_mines)
        self.clock_label.display(0)
    
    def handle_restart_button(self):
        self.create_new_game(Vector2(Settings.SIZE[0], Settings.SIZE[1]), Settings.MINES)

    def update_time(self):
        self.timer_counter += 1
        self.clock_label.display(self.timer_counter)

    def edit_mine_count(self, count):
        self.current_mines += count
        self.mines_label.display(self.current_mines)

    def set_game_over(self):
        self.timer.stop()
        self.restart_btn.setStyleSheet(self.ctx.faces['FACE_DEAD'])

    def set_win(self):
        self.timer.stop()
        self.restart_btn.setStyleSheet(self.ctx.faces['FACE_WIN'])

    def set_button_style_pressed(self):
        self.restart_btn.setStyleSheet(self.ctx.faces['FACE_CLICKED'])
    
    def set_button_style_normal(self):
        self.restart_btn.setStyleSheet(self.ctx.faces['FACE_NORMAL'])

    def set_button_style_danger(self):
        self.restart_btn.setStyleSheet(self.ctx.faces['FACE_DANGER'])