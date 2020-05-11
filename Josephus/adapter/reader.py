from shared import serializers as srlz

import csv
import os
import zipfile



class TxtReader(srlz.Reader):
    def __init__(self, path):
        self.file = open(path, 'r', encoding='utf-8')
        self._all_data = self.file.readlines()

    def create_person_from_file(self):
        for each in self._all_data:
            data = each.strip().replace(' ','').split(',')
            name = data[0]
            try:
                age = int(data[1])
            except ValueError as e:
                age = 'ValueError'
            gender = data[2]
            yield Person(name, age, gender)

    def __len__(self):
        return len(self._all_data)

    def close_file(self):
        self.file.close()
        
class CsvReader(srlz.Reader):
    def __init__(self, path):
        self.file = open(path, 'r', encoding='gbk')
        self._all_data = self.file.readlines()

    def create_person_from_file(self):
        for each in self._all_data:
            data = each.strip().replace(' ','').split(',')
            name = data[0]
            try:
                age = int(data[1])
            except ValueError as e:
                age = -1
            gender = data[2]
            yield Person(name, age, gender)

    def __len__(self):
        return len(self._all_data)

    def close_file(self):
        self.file.close()

class ZipReader(srlz.Reader):
    def __init__(self, path, file_name):
        with zipfile.ZipFile(path, 'r') as zip_file:
            file_list = zip_file.namelist()
            if file_name not in file_list:
                raise FileNotFoundError

            file_path = zip_file.extract(file_name)
            file_type = file_name.split('.')[1]
            if file_type == 'txt':
                encode_standard = 'utf-8'
            if file_type == 'csv':
                encode_standard = 'gbk'

            self.file = open(file_path, 'r', encoding = encode_standard)
            self._all_data = self.file.readlines()

    def create_person_from_file(self):
        for each in self._all_data:
            data = each.strip().replace(' ','').split(',')
            name = data[0]
            try:
                age = int(data[1])
            except ValueError as e:
                age = 'ValueError'
            gender = data[2]
            yield Person(name, age, gender)
            
    def __len__(self):
        return len(self._all_data)

    def close_file(self):
        self.file.close()