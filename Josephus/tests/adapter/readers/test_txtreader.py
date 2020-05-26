from domain.adapter.readers import readers as rds
from domain.shared.person import Person
from typing import List
        

def test_read_txt_file():
    path = 'data\\people.txt'
    txtreader = rds.TxtReader(path)
    reader = txtreader.create_person_from_file()
    
    assert reader == [
        Person('Morty', 12, 'male'),
        Person('Rick', 53, 'male'),
        Person('Summer', 16, 'female'),
        Person('Beth', 34, 'female'),
        Person('Jerry', 36, 'male'),
    ]