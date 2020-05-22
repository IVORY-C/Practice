from domain.adapter import readers as rds
from domain.shared import base_class as bc
from typing import List
        

def test_read_txt_file():
    path = 'data\\people.txt'
    txtreader = rds.TxtReader(path)
    reader = txtreader.create_person_from_file()
    
    assert reader[0].name == 'Morty'
    assert reader[1].name == 'Rick'
    assert reader[2].age == 16
    assert reader[3].gender == 'female'
    assert reader[4].gender == 'male'