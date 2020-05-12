from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile

from main.shared import base_class as bc
from main.use_cases import josephus as jsp

class test_ui(object):
    def __init__(self):
        self.ui = QUiLoader().load('main_window.ui')

        self.ui.input_people_button.clicked.connect(self.handleCalc)

    def handleCalc(self):
        info = self.ui.people_text.toPlainText()

        reader = []
        for line in info.splitlines():
            if not line.strip():
                continue
            data = line.split(',')
            name = data[0]
            age = data[1]
            gender = data[2]
            reader.append(Person(name, age, gender))

        ring = jsp.Ring(reader)
        result = ''
        for item in ring:
            data_str = 

        QMessageBox.about(self.ui,
                    '出列顺序',
                    f'''薪资20000 以上的有：\n{salary_above_20k}
                    \n薪资20000 以下的有：\n{salary_below_20k}'''
                    )


