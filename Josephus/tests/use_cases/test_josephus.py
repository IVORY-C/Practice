from main.shared import base_class as bc
from main.use_cases import josephus as jsp


def test_josephus():
    reader = []
    reader.append(bc.Person('Morty', 12, 'male'))
    reader.append(bc.Person('Rick', 53, 'male'))
    reader.append(bc.Person('Summer', 16, 'female'))
    reader.append(bc.Person('Beth', 34, 'female'))
    reader.append(bc.Person('Jerry', 36, 'male'))

    ring = jsp.Ring(reader)
    ring.start = 2
    ring.step = 5
    ring.reset()

    result_name = []
    result_age =[]
    result_gender = []
    for item in ring:
        result_name.append(item.name)
        result_age.append(item.age)
        result_gender.append(item.gender)

    assert result_name == ['Rick', 'Summer', 'Jerry', 'Morty', 'Beth']
    assert result_age == [53, 16, 36, 12, 34]
    assert result_gender == ['male', 'female', 'male', 'male', 'female']