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
        self.restart_btn = QPushButton('Restart')
        self.restart_btn.clicked.connect(self.handle_restart_button)
        self.top_layout.addWidget(self.restart_btn)

        # Clock
        self.clock_label = QLCDNumber()
        self.clock_label.setSegmentStyle(QLCDNumber.Flat)

        # TODO: fix connect signal
        self.timer = QTimer()
        self.clock_label.connect(self.timer, SIGNAL('timeout()'), self.update_time)

        self.top_layout.addWidget(self.clock_label)
        self.addLayout(self.top_layout)

    def start_timer(self):
        self.timer.start(1000)

    def stop_timer(self):
        self.timer.stop()

    def create_new_game(self, size, mines):
        # TODO: resize window to fit mines without border
        if hasattr(self, 'board'):
            self.board.unload_board()
            self.removeItem(self.board.layout)

        self.game_over = False
        self.timer_counter = 0
        self.current_mines = mines
        
        self.board = Board(self.ctx, self, size, mines)
        self.addLayout(self.board.layout)
        self.update_top_layout()

    def update_top_layout(self):
        self.mines_label.display(self.current_mines)
        self.clock_label.display(0)
    
    # TODO: remove hard count
    def handle_restart_button(self):
        self.create_new_game(Vector2(15, 15), 10)

    def update_time(self):
        self.timer_counter += 1
        self.clock_label.display(self.timer_counter)

    def edit_mine_count(self, count):
        self.current_mines += count
        self.mines_label.display(self.current_mines)

    def set_game_over(self):
        self.stop_timer()
        # TODO: on screen report
