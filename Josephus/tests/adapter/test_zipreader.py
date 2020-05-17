from main.shared import reader as rd
from main.shared import base_class as bc

import zipfile

class ZipReader(rd.Reader):
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
        people = []
        for each in self._all_data:
            data = each.strip().replace(' ','').split(',')
            name = data[0]
            try:
                age = int(data[1])
            except ValueError as e:
                age = -2
            gender = data[2]
            people.append(bc.Person(name, age, gender))

        return people   

            
    def __len__(self):
        return len(self._all_data)

    def close_file(self):
        self.file.close()


path = 'data\\people.zip'
file_name = 'people.txt'
zipreader = ZipReader(path, file_name)
reader = zipreader.create_person_from_file()

assert reader[0].name == 'Morty'
assert reader[1].name == 'Rick'
assert reader[2].age == 16
assert reader[3].gender == 'female'
assert reader[4].gender == 'male'