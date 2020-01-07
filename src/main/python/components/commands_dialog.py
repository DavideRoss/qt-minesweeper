from PySide2.QtWidgets import *

class CommandsDialog(QDialog):

    def __init__(self, parent=None):
        super(CommandsDialog, self).__init__(parent)

        self.setWindowTitle('Help - Minesweeper')
        self.setFixedSize(self.minimumSizeHint())

        self.main_layout = QVBoxLayout()

        self.commands_title = QLabel('Commands')
        self.commands_title.setStyleSheet('font-weight: bold; font-size: 18px')
        self.main_layout.addWidget(self.commands_title)

        self.commands_layout = QFormLayout()
        self.commands_layout.addRow(self.tr('Left click:'), QLabel('Reveal an empty square'))
        self.commands_layout.addRow(self.tr('Right click:'), QLabel('Flag an empty square'))
        self.commands_layout.addRow(self.tr('Middle click:'), QLabel('Click on a number to reveal adjacent squares'))
        self.main_layout.addLayout(self.commands_layout)

        self.settings_title = QLabel('Settings')
        self.settings_title.setStyleSheet('font-weight: bold; font-size: 18px')
        self.main_layout.addWidget(self.settings_title)

        self.settings_label = QLabel('Edit config.ini file and restart the application to edit the game rules.')
        self.main_layout.addWidget(self.settings_label)

        self.settings_layout = QFormLayout()
        self.settings_layout.addRow(self.tr('size_x:'), QLabel('Number of rows of the grid'))
        self.settings_layout.addRow(self.tr('size_y:'), QLabel('Number of columns of the grid'))
        self.settings_layout.addRow(self.tr('mines:'), QLabel('Number of mines distributed on the grid'))
        self.main_layout.addLayout(self.settings_layout)

        self.setLayout(self.main_layout)
