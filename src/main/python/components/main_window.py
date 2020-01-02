# TODO: clean unused
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from components import *
from settings import Settings
from utils import Vector2

class MainWindow(QMainWindow):

    def __init__(self, ctx):
        super(MainWindow, self).__init__()

        self.ctx = ctx
        self.setWindowTitle('Minesweeper')
        self.setWindowIcon(ctx.app_icon)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        self.create_actions()
        self.create_menus()

        self.game_layout = GameLayout(self.ctx)
        # TODO: load from last setting
        # self.game_layout.create_new_game(Vector2(Settings.SIZE[0], Settings.SIZE[1]), Settings.MINES)
        self.game_layout.create_new_game(Vector2(Settings.SIZE[0], Settings.SIZE[1]), 10)

        main_widget.setLayout(self.game_layout)

    def closeEvent(self, e):
        Settings.write_file(self.ctx)
    
    def create_actions(self):
        self.newGameAct = QAction('&New', self, shortcut=QKeySequence('F2'), triggered=self.new_game)

        self.newGameBeginnerAct = QAction('&Beginner', self, triggered=self.new_game_beginner, checkable=True)
        self.newGameIntermediateAct = QAction('&Intermediate', self, triggered=self.new_game_intermediate, checkable=True)
        self.newGameExpertAct = QAction('&Expert', self, triggered=self.new_game_expert, checkable=True)
        self.newGameCustomAct = QAction('&Custom...', self, triggered=self.new_game_custom, checkable=True)
        self.bestTimesAct = QAction('Best &Times...', self, triggered=self.show_best_times)
        self.exitGameAct = QAction('E&xit', self, triggered=self.exit_game)

        self.helpAct = QAction('&Commands...', self, shortcut=QKeySequence('F1'), triggered=self.show_help_window)
        self.aboutAct = QAction('&About Minesweeper...', self, triggered=self.show_about_window)

        self.difficultyGroup = QActionGroup(self)
        self.difficultyGroup.addAction(self.newGameBeginnerAct)
        self.difficultyGroup.addAction(self.newGameIntermediateAct)
        self.difficultyGroup.addAction(self.newGameExpertAct)
        self.difficultyGroup.addAction(self.newGameCustomAct)

        if Settings.DIFFICULTY_SETTING == 0:
            self.newGameBeginnerAct.setChecked(True)
        elif Settings.DIFFICULTY_SETTING == 1:
            self.newGameIntermediateAct.setChecked(True)
        elif Settings.DIFFICULTY_SETTING == 2:
            self.newGameExpertAct.setChecked(True)
        else:
            self.newGameCustomAct.setChecked(True)

    def create_menus(self):
        self.game_menu = self.menuBar().addMenu('&Game')
        self.game_menu.addAction(self.newGameAct)
        self.game_menu.addSeparator()
        self.game_menu.addAction(self.newGameBeginnerAct)
        self.game_menu.addAction(self.newGameIntermediateAct)
        self.game_menu.addAction(self.newGameExpertAct)
        self.game_menu.addAction(self.newGameCustomAct)
        self.game_menu.addSeparator()
        self.game_menu.addAction(self.bestTimesAct)
        self.game_menu.addSeparator()
        self.game_menu.addAction(self.exitGameAct)

        self.help_menu = self.menuBar().addMenu('&Help')
        self.help_menu.addAction(self.helpAct)
        self.help_menu.addSeparator()
        self.help_menu.addAction(self.aboutAct)

    # TODO: implement
    def new_game(self):
        # print('new game same settings')
        self.game_layout.create_new_game(Vector2(15, 15), 1)

    # TODO: implement
    def new_game_beginner(self):
        self.game_layout.create_new_game(Vector2(9, 9), 10)
        Settings.DIFFICULTY_SETTING = 0

    # TODO: implement
    def new_game_intermediate(self):
        self.game_layout.create_new_game(Vector2(16, 16), 40)
        Settings.DIFFICULTY_SETTING = 1

    # TODO: implement
    def new_game_expert(self):
        self.game_layout.create_new_game(Vector2(16, 30), 99)
        Settings.DIFFICULTY_SETTING = 2

    # TODO: implement
    def new_game_custom(self):
        print('new_game_custom')
        Settings.DIFFICULTY_SETTING = 3

    # TODO: implement
    def show_best_times(self):
        print('best_times')

    # TODO: implement
    def exit_game(self):
        print('exit')

    # TODO: implement
    def show_help_window(self):
        print('show help')

    # TODO: implement
    def show_about_window(self):
        print('show about')