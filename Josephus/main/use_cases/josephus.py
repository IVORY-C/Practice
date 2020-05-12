import copy

class Josephus:
    '约瑟夫环'

    def __init__(self, reader = None):
        self._people = []
        if reader:
            for each in reader:
                self._people.append(each)
        self.step = 0
        self.start = 1


    def append(self, obj):
        self._people.append(obj)

    def pop(self):
        self._people.pop(0)

    def query_list(self):
        return self._people

    def __len__(self):
        return len(self._people)

    def next_bymod(self):
        temp = copy.copy(self._people)
        length = len(temp)
        if length == 0:
            return None
        id_ = self.start

        for i in range(length):
            id_ = (id_ + self.step - 1) % len(temp)
            index = temp.pop(id_)
            yield index

    def next_circular(self):
        temp = copy.copy(self._people)
        if len(temp) == 0:
            return None

        index = 1
        start = self.start % len(temp)
        temp = temp[start:] + temp[:start]

        while index:
            head = (self.step-1) % len(temp)
            temp = temp[head:] + temp[:head]
            index = temp.pop(0)
            yield index
