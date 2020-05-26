from domain.use_cases import josephus as jsp
from domain.adapter.readers import readers as rds
from domain.shared.person import Person

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit,QMessageBox
from typing import List

class UIQt():
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

        reader = []
        result_str = ''
        if people:
            for line in people.splitlines():
                if not line.strip():
                    continue
                data = line.split(',')
                name = data[0]
                age = int(data[1])
                gender = data[2]
                reader.append(Person(name, age, gender)) 
                
        if path:
            file_type = file_name.split('.')[1]
            if file_type == 'txt':
                file_reader = rds.TxtReader(path)
            if file_type == 'csv':
                file_reader = rds.CsvReader(path)
            if file_type == 'zip':
                file_reader = rds.ZipReader(path, file_name)

            reader = file_reader.create_person_from_file()

        if reader:
            ring = jsp.Ring(reader)
            ring.start = int(start)
            ring.step = int(step)
            ring.reset()

            result_str = ''
            for item in ring:
                item_str = f"Name:{item.name}, Age:{item.age}, Gender:{item.gender}"
                result_str += item_str + '\n'            
        
        else:
            result_str = 'No data input'

        QMessageBox.about(self.window, 
                    'Result' , 
                    f"The result is:\n{result_str}\n start: {start}\n step: {step}")






