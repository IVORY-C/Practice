from domain.shared import base_class as bc
from domain.use_cases import josephus as jsp
from domain.adapter import readers as rd

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

        reader = []
        result_str = ''
        if people:
            for line in people.splitlines():
                if not line.strip():
                    continue
                data = line.split(',')
                name = data[0]
                age = data[1]
                gender = data[2]
                reader.append(bc.Person(name, age, gender))

        else :
            file_type = file_name.split('.')[1]
            if file_name == 'txt':
                file_reader = rd.TxtReader(path)
            elif file_name == 'csv':
                file_reader = rd.CsvReader(path)
            elif: file_name == 'zip':
                file_reader = rd.ZipReader(path, file_name)
            else:
                raise(ValueError)
            reader = zipreader.create_person_from_file()

            
        ring = jsp.Ring(reader)
        ring.reset()
        ring.start = start
        ring.step = step

        for item in ring:
            data_str : str = item.name + ', age: {}, gender: {}'.format(item.age, item.gender)  
            result_str += data_str + '\n'
            

        QMessageBox.about(self.window, 'Result' , result_str)

