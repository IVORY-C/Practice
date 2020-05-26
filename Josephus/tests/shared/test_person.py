from domain.shared.person import Person

def test_Person_with_correct_parameters():
    someone = Person('Beth', 10, 'female')

    assert someone.name == 'Beth'
    assert someone.age == 10
    assert someone.gender == 'female'

def test_Person_without_parameters():
    someone = Person()

    assert someone.name == None
    assert someone.age == 0
    assert someone.gender == 'ValueError'

def test_Person_with_age_less_than_zero():
    someone = Person(age=-10)

    assert someone.age == Person.INVALID_AGE_LESS_THAN_ZERO

def test_Person_with_gender_is_not_male_or_female():
    someone = Person(gender='test')

    assert someone.gender == 'ValueError'


