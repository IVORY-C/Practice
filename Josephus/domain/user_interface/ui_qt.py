from domain.use_cases import josephus as jsp
from domain.adapter.readers import readers as rds
from domain.shared.person import Person
from domain.user_interface.process_data_and_output import ProcessDataAndOutput

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
        process = ProcessDataAndOutput()

        process.people_text = self.people_text.toPlainText()
        process.path = self.path_text.toPlainText()
        process.file_name = self.file_name_text.toPlainText()
        try:
            start = int(self.start_text.toPlainText())
            step = int(self.start_text.toPlainText())
            process.start = start
            process.step = step
        except ValueError as e:
            raise ValueError('Start and step must be integer!')

        result_str = process.output_result_str().replace('; ', '\n')

        QMessageBox.about(self.window, 
                    'Result', 
                    f"The result is:\n{result_str}\n start: {process.start}\n step: {process.step}")






