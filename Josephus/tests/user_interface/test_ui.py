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
        info = self.people_text.toPlainText()

        result = ''
        for line in info.splitlines():
            if not line.strip():
                continue
            data = line.split(',')
            result += data[0] + '\n'
            

        QMessageBox.about(self.window, 'Result' , result)

app = QApplication([])
stats = test_ui()
stats.window.show()
app.exec_()





