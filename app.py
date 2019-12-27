import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from classes import *
import res

def main():
    app = QApplication(sys.argv)
    main_layout = GameLayout()
    res.init()

    window = QWidget()
    window.setWindowTitle('Minesweeper')

    window.setWindowIcon(res.icons['ICON_MINE_TRANSPARENT'])
    window.setLayout(main_layout)
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()