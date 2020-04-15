# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
class Person(object):
    def __init__(self):
        self.name = 0
        self.age = 0
        self.gender = 0


# %%
class Josephus:
    '约瑟夫环'

    def __init__(self):
        self.people = []
        self.step = 0
        self.start = 1

        self.temp = self.people
        self.current_id = 0
        self.length = 0

    def append(self, obj):
        self.people.append(obj)

    def pop(self):
        self.people.pop(0)

    def query_list(self):
        return self.people

    def reset(self):
        import copy
        self.current_id = self.start
        self.temp = copy.copy(self.people)
        self.length = len(self.people)

    def next_bymod(self):
        length = len(self.temp)
        if length == 0:
            return None

        id_ = (self.current_id + self.step - 1) % length
        index = self.temp.pop(id_)
        self.current_id = id_

        return index

    def next_circular(self):
        length = len(self.temp)
        if length == 0:
            return None

        id_ = (self.current_id + self.step - 1) % length
        self.temp = self.temp[id_:] + self.temp[:id_]
        index = self.temp.pop(0)
        self.current_id = id_

        return index


    def create_generator(self):
        length = len(self.temp)
        id_ = self.start

        for i in range(length):
            id_ = (id_ + self.step - 1) % len(self.temp)
            index = self.temp.pop(id_)
            yield index


# %%
def create_person(name, age, gender):
    obj = Person()
    obj.name = name
    obj.age = age 
    obj.gender = gender
    
    return obj
    


# %%
ring = Josephus()
ring.start = 6
ring.step = 3

ring.append(create_person('Morty', 12, '男'))
ring.append(create_person('Rick', 53, '男'))
ring.append(create_person('Summer', 16, '女'))
ring.append(create_person('Beth', 34, '女'))
ring.append(create_person('Jerry', 36, '男'))


# %%
#使用生成器
ring.reset()
generator = ring.create_generator()

for i in range(ring.length):
    index = next(generator)
    print("第{}个出列的人：{}；年龄：{}；性别：{}". format(i+1, index.name, index.age, index.gender))


# %%
ring.reset()
for i in range(ring.length):
    index = ring.next_bymod()
    if index:
        print("第{}个出列的人：{}；年龄：{}；性别：{}". format(i+1, index.name, index.age, index.gender))

print('-'*30)

ring.reset()
for i in range(ring.length):
    index = ring.next_circular()
    if index:
        print("第{}个出列的人：{}；年龄：{}；性别：{}". format(i+1, index.name, index.age, index.gender))


# %%


