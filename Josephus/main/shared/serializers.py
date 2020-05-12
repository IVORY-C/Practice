class Reader:
    def create_person_from_file(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def close_file(self):
        raise NotImplementedError