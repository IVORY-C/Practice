import copy

class Ring:
    '约瑟夫环'

    def __init__(self, reader=None):
        self._people = []
        self._temp = []
        self._id = 0

        if reader:
            for each in reader:
                self._people.append(each)
        self.step = 1
        self.start = 1


    def append(self, obj):
        self._people.append(obj)

    def pop(self):
        self._people.pop(0)

    def query_list(self):
        return self._people

    def __len__(self):
        return len(self._people)

    def reset(self):
        self._temp = copy.copy(self._people)
        self._id = copy.copy(self.start)

    def __iter__(self):
        return self

    def __next__(self):
        if self._temp:
            self._id = (self._id + self.step - 1) % len(self._temp)
            out = self._temp.pop(self._id)
            return out
        raise StopIteration()
   

