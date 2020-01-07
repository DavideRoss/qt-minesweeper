from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

class InfoDialog(QDialog):

    def __init__(self, ctx, parent=None):
        super(InfoDialog, self).__init__(parent)

        self.ctx = ctx
        self.setWindowTitle('About - Minesweeper')
        self.setFixedSize(self.minimumSizeHint())

        self.main_layout = QHBoxLayout()

        self.icon_img = QPixmap(self.ctx.get_resource('mine_small.png'))
        self.icon_label = QLabel()
        self.icon_label.setPixmap(self.icon_img)
        self.icon_label.setGeometry(QRect(0, 0, 128, 128))
        self.icon_label.setAlignment(Qt.AlignTop)
        self.main_layout.addWidget(self.icon_label)

        self.credits_layout = QVBoxLayout()

        self.credits_title_label = QLabel('Minesweeper')
        self.credits_title_label.setStyleSheet('font-weight: bold; font-size: 18px')
        self.credits_layout.addWidget(self.credits_title_label)

        self.credits_label = QLabel('2019-2020 Davide Rossetto')
        self.art_label = QLabel('Art assets taken from <a href=\'http://minesweeperonline.com/\'>http://minesweeperonline.com</a>')
        self.art_label.setOpenExternalLinks(True)
        self.git_label = QLabel('Source code available at <a href=\'https://github.com/DavideRoss/qt-minesweeper/\'>https://github.com/DavideRoss/qt-minesweeper</a>')
        self.git_label.setOpenExternalLinks(True)
        
        self.credits_layout.addWidget(self.credits_label)
        self.credits_layout.addWidget(self.art_label)
        self.credits_layout.addWidget(self.git_label)

        self.main_layout.addLayout(self.credits_layout)

        self.setLayout(self.main_layout)