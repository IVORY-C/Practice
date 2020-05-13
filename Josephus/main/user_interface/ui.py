from main.shared import base_class as bc
from main.use_cases import josephus as jsp

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit,QMessageBox

class test_ui():
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(500, 400)
        self.window.move(300, 300)
        self.window.setWindowTitle('Josephus')

        self.people_text = QPlainTextEdit(self.window)
        self.people_text.setPlaceholderText("Please input people")
        self.people_text.move(10, 25)
        self.people_text.resize(300, 350)

        self.start_text = QPlainTextEdit(self.window)
        self.start_text.setPlaceholderText("Please input start number")
        self.start_text.move(330, 25)
        self.start_text.resize(150, 100)

        self.step_text = QPlainTextEdit(self.window)
        self.step_text.setPlaceholderText("Please input step")
        self.step_text.move(330, 150)
        self.step_text.resize(150, 100)

        self.button = QPushButton('Result', self.window)
        self.button.move(350, 300)

        self.button.clicked.connect(self.handle_button)


    def handle_button(self):
        people_info = self.people_text.toPlainText()
        start_info = self.start_text.toPlainText()
        step_info = self.step_text.toPlainText()

        reader = []
        result = ''
        for line in people_info.splitlines():
            if not line.strip():
                continue
            data = line.split(',')
            name = data[0]
            age = data[1]
            gender = data[2]
            reader.append(bc.Person(name, age, gender))

        ring = jsp.Ring(reader)
        ring.reset()
        ring.start = start_info
        ring.step = step_info

        for item in ring:
            data_str : str = item.name + ', age: {}, gender: {}'.format(item.age, item.gender)  
            result += data_str + '\n'
            

        QMessageBox.about(self.window, 'Result' , result)

app = QApplication([])
stats = test_ui()
stats.window.show()
app.exec_()