class Person(object):
    INVALID_AGE_LESS_THAN_ZERO = -1
    INVALID_AGE_IS_NOT_INT = -2

    INVALID_GENDER = 'ValueError'
    def __init__(self, name: str = None, age: int = 0, gender: str = None):
        self.name = name
        self.age = age
        self.gender = gender

        if self.age < 0 :
            self.age = Person.INVALID_AGE_LESS_THAN_ZERO

        if self.gender not in ['male', 'female']:
            self.gender = Person.INVALID_GENDER

    def __eq__(self, obj) -> bool:
        if (obj.name == self.name) & (obj.age == self.age) & (obj.gender == self.gender):
            return True
        else:
            return False