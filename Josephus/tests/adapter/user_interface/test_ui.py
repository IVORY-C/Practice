from domain.use_cases import josephus as jsp
from domain.adapter.readers import readers as rds
from domain.shared.person import Person
from domain.user_interface.ui_qt import UIQt


def test_ui_input_and_show_data():
    app = QApplication([])
    stats = UIQt()
    stats.window.show()
    app.exec_()





