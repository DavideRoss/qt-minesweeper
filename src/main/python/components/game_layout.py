from PySide2.QtWidgets import *
from PySide2.QtCore import *

from components import Board
from utils import Vector2
from settings import *

class GameLayout(QVBoxLayout):

    def __init__(self, ctx, parent=None):
        super(GameLayout, self).__init__(parent)

        self.ctx = ctx

        # TODO: reset on new game
        self.current_mines = MINES
        self.game_over = False
        
        self.create_board()
        self.init_ui()

    def init_ui(self):
        self.timer_counter = 0

        top_layout = QHBoxLayout()

        self.mines_label = QLCDNumber()
        self.mines_label.display(self.current_mines)
        self.mines_label.setSegmentStyle(QLCDNumber.Flat)
        top_layout.addWidget(self.mines_label)

        restart_btn = QPushButton('Restart')
        restart_btn.clicked.connect(self.handle_restart_button)
        top_layout.addWidget(restart_btn)

        self.clock_label = QLCDNumber()
        self.clock_label.display(0)
        self.clock_label.setSegmentStyle(QLCDNumber.Flat)

        # TODO: fix connect signal
        # TODO: start on first click
        self.timer = QTimer()
        self.clock_label.connect(self.timer, SIGNAL('timeout()'), self.update_time)
        self.timer.start(1000)

        top_layout.addWidget(self.clock_label)

        # self.addWidget(menuBar)
        self.addLayout(top_layout)
        self.addLayout(self.board.layout)
    
    def create_board(self):
        self.board = Board(self.ctx, self, Vector2(SIZE[0], SIZE[1]))

    def handle_restart_button(self):
        self.board.create_board()
        self.board.update_layout()

    def update_time(self):
        self.timer_counter += 1
        self.clock_label.display(self.timer_counter)

    def edit_mine_count(self, count):
        self.current_mines += count
        self.mines_label.display(self.current_mines)

    def set_game_over(self):
        self.game_over = True
        self.timer.stop()
        # TODO: on screen report
