import sys

from domain.user_interface.ui_qt import UIQt
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    stats = UIQt()
    stats.window.show()
    app.exec_()