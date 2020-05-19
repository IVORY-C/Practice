from main.use_cases import josephus as jsp
from main.adapter import readers as rd

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
        self.people_text.resize(300, 150)

        self.start_text = QPlainTextEdit(self.window)
        self.start_text.setPlaceholderText("Please input start number")
        self.start_text.move(330, 25)
        self.start_text.resize(150, 100)

        self.step_text = QPlainTextEdit(self.window)
        self.step_text.setPlaceholderText("Please input step")
        self.step_text.move(330, 150)
        self.step_text.resize(150, 100)

        self.path_text = QPlainTextEdit(self.window)
        self.path_text.setPlaceholderText("Please input path")
        self.path_text.move(10, 200)
        self.path_text.resize(300, 80)

        self.file_name_text = QPlainTextEdit(self.window)
        self.file_name_text.setPlaceholderText("Please input file name")
        self.file_name_text.move(10, 300)
        self.file_name_text.resize(300, 80)

        self.button = QPushButton('Result', self.window)
        self.button.move(350, 300)

        self.button.clicked.connect(self.handle_button)


    def handle_button(self):
        people = self.people_text.toPlainText()
        start = self.start_text.toPlainText()
        step = self.step_text.toPlainText()
        path = self.path_text.toPlainText()
        file_name = self.file_name_text.toPlainText()

        result = ''
        if people:
            for line in people.splitlines():
                if not line.strip():
                    continue
                data = line.split(',')
                data_str = f"Name: {data[0]}, Age: {data[1]}, Gender: {data[2]}"
                result += data_str + '\n'

        elif path:
            file_type = file_name.split('.')[1]
            if file_type == 'txt':
                file_reader = rds.TxtReader(path)
            if file_type == 'csv':
                file_reader = rds.CsvReader(path)
            if file_type == 'zip':
                file_reader = rds.ZipReader(path)
                
            reader = file_reader.create_person_from_file()
            for each in reader:
                data_str = f"Name: {each.name}, Age: {each.age}, Gender: {each.gender}"
                result += data_str + '\n'
        else:
            result = 'No data input'
            

        QMessageBox.about(self.window, 
                    'Result' , 
                    f"The result is:\n{result}\n start: {start}\n step: {step}")


def test_ui_input_and_show_data():
    app = QApplication([])
    stats = test_ui()
    stats.window.show()
    app.exec_()





