from PySide2.QtWidgets import *
from PySide2.QtCore import *

from classes import Board, Vector2
from settings import *

class GameLayout(QVBoxLayout):

    def __init__(self, parent=None):
        super(GameLayout, self).__init__(parent)

        self.create_board()
        self.init_ui()

    def init_ui(self):
        self.timer_counter = 0

        top_layout = QHBoxLayout()

        mines_label = QLCDNumber()
        mines_label.display(MINES)
        mines_label.setSegmentStyle(QLCDNumber.Flat)
        top_layout.addWidget(mines_label)

        restart_btn = QPushButton('Restart')
        restart_btn.clicked.connect(self.handle_restart_button)
        top_layout.addWidget(restart_btn)

        self.clock_label = QLCDNumber()
        self.clock_label.display(0)
        self.clock_label.setSegmentStyle(QLCDNumber.Flat)

        # TODO: fix connect signal
        self.timer = QTimer()
        self.clock_label.connect(self.timer, SIGNAL('timeout()'), self.update_time)
        self.timer.start(1000)

        top_layout.addWidget(self.clock_label)

        self.addLayout(top_layout)
        self.addLayout(self.board.layout)
    
    def create_board(self):
        self.board = Board(Vector2(SIZE[0], SIZE[1]))

    def handle_restart_button(self):
        self.board.create_board()
        self.board.update_layout()

    def update_time(self):
        self.timer_counter += 1
        self.clock_label.display(self.timer_counter)

