import sys
from PySide2.QtWidgets import *
from PySide2.QtCore import *

from classes import *

def main():
    app = QApplication(sys.argv)
    main_layout = GameLayout()

    window = QWidget()
    window.setLayout(main_layout)
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()