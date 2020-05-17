from main.shared import reader as rd
from main.shared import base_class as bc

class TxtReader(rd.Reader):
    def __init__(self, path):
        self.file = open(path, 'r', encoding='utf-8')
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
        

path = 'data\\people.txt'
txtreader = TxtReader(path)
reader = txtreader.create_person_from_file()

assert reader[0].name == 'Morty'
assert reader[1].name == 'Rick'
assert reader[2].age == 16
assert reader[3].gender == 'female'
assert reader[4].gender == 'male'