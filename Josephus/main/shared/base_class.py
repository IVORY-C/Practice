class Person(object):
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender
        if self.age < 0 :
            self.age = -1

        if self.gender not in ['male', 'female']:
            self.gender = 'ValueError'

    def __eq__(self, obj):
        if (obj.name == self.name) & (obj.age == self.age) & (obj.gender == self.gender):
            return True
        else:
            return False