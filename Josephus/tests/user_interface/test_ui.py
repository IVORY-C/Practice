from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit,QMessageBox

class test_ui():
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(500, 400)
        self.window.move(300, 300)
        self.window.setWindowTitle('Josephus')

        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.setPlaceholderText("Please input people")
        self.textEdit.move(10, 25)
        self.textEdit.resize(300, 350)

        self.button = QPushButton('Result', self.window)
        self.button.move(380, 80)

        self.button.clicked.connect(self.handle_button)


    def handle_button(self):
        info = self.textEdit.toPlainText()

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





