from domain.adapter.readers import readers as rds
from domain.shared.person import Person
from typing import List

import zipfile

def test_read_zip_file():
    path = 'data\\people.zip'
    file_name = 'people.txt'
    zipreader = rds.ZipReader(path, file_name)
    reader = zipreader.create_person_from_file()

    assert reader == [
        Person('Morty', 12, 'male'),
        Person('Rick', 53, 'male'),
        Person('Summer', 16, 'female'),
        Person('Beth', 34, 'female'),
        Person('Jerry', 36, 'male'),
    ]