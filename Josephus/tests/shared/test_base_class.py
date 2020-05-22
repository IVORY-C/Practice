from domain.shared import base_class as bc

def test_base_class():
    test_someone = bc.Person('Andy', 12, 'male')
    test_someone_age_error = bc.Person('Beth', -10, 'female')
    test_someone_gender_error = bc.Person('Cindy', 24, 'a')

    assert test_someone.name == 'Andy'
    assert test_someone.age == 12
    assert test_someone.gender == 'male'

    assert test_someone_age_error.age == -1
    assert test_someone_gender_error.gender == 'ValueError'
