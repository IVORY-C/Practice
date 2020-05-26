import sys
sys.path.append("C:\\Users\\76747\\Desktop\\Python\\practice\\Josephus")

from domain.user_interface.ui_qt import UIQt
from PySide2.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    stats = UIQt()
    stats.window.show()
    app.exec_()