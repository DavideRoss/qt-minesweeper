from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from components import *
from settings import Settings
from utils import Vector2

from components.commands_dialog import CommandsDialog
from components.info_dialog import InfoDialog

class MainWindow(QMainWindow):

    def __init__(self, ctx):
        super(MainWindow, self).__init__()

        self.ctx = ctx
        self.setWindowTitle('Minesweeper')
        self.setWindowIcon(ctx.app_icon)

        self.setWindowFlags(self.windowFlags() | Qt.CustomizeWindowHint)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        self.setFixedSize(self.minimumSizeHint())

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        self.create_actions()
        self.create_menus()

        self.game_layout = GameLayout(self.ctx)
        self.game_layout.create_new_game(Vector2(Settings.SIZE[0], Settings.SIZE[1]), Settings.MINES)

        main_widget.setLayout(self.game_layout)

    def closeEvent(self, e):
        Settings.write_file(self.ctx)
    
    def create_actions(self):
        self.newGameAct = QAction('&New', self, shortcut=QKeySequence('F2'), triggered=self.new_game)
        self.exitGameAct = QAction('E&xit', self, triggered=self.exit_game)

        self.helpAct = QAction('&Commands...', self, shortcut=QKeySequence('F1'), triggered=self.show_help_window)
        # TODO: remove shortcut
        self.aboutAct = QAction('&About Minesweeper...', self, shortcut=QKeySequence('F3'), triggered=self.show_about_window)

    def create_menus(self):
        self.game_menu = self.menuBar().addMenu('&Game')
        self.game_menu.addAction(self.newGameAct)
        self.game_menu.addSeparator()
        self.game_menu.addAction(self.exitGameAct)

        self.help_menu = self.menuBar().addMenu('&Help')
        self.help_menu.addAction(self.helpAct)
        self.help_menu.addSeparator()
        self.help_menu.addAction(self.aboutAct)

    def new_game(self):
        self.game_layout.create_new_game(Vector2(Settings.SIZE[0], Settings.SIZE[1]), Settings.MINES)

    def exit_game(self):
        self.close()

    def show_help_window(self):
        cmdDialog = CommandsDialog(self)
        cmdDialog.exec_()

    def show_about_window(self):
        infoDialog = InfoDialog(self.ctx, self)
        infoDialog.exec_()