from domain.shared.person import Person
from domain.adapter.readers import readers as rds
from domain.use_cases import josephus as jsp

class ProcessDataAndOutput():
    def __init__(self):
        self.people_text = ''
        self.path = ''
        self.file_name = ''
        self.result = []
        self.start = 1
        self.step = 1

    def output_result_str(self):
        if self.people_text and self.path:
            raise ValueError('Cannot input both people and file path!')

        if self.people_text and not self.path:
            reader = self.input_people_text()

        if self.path and not self.people_text:
            reader = self.input_path()
    
        result_str = self.create_ring_and_output_result(reader)
        return result_str

    def input_people_text(self):
        try:
            people_str = self.people_text.split(';')
            for each in people_str:
                if not each:
                    continue 
                data = each.replace(' ','').strip().split(',')
                name = data[0]
                try:
                    age = int(data[1])
                except:
                    age = -1
                gender = data[2]
                reader.append(Person(name, age, gender))
        except:
            raise ValueError('Input incorrect data of people!')
        else:
            return reader


    def input_path(self):
        try:
            file_type = self.path.split('.')[-1]

            if file_type == 'txt':
                file_reader = rds.TxtReader(self.path)
            if file_type == 'csv':
                file_reader = rds.CsvReader(self.path)
            if file_type == 'zip':
                file_reader = rds.ZipReader(self.path, self.file_name)

            reader = file_reader.create_person_from_file()
        except:
            raise ValueError('Input incorrect path or file_name!')
        else:
            return reader

    def create_ring_and_output_result(self, reader):
        result_str = ''
        if reader:
            ring = jsp.Ring(reader)
            ring.start = self.start
            ring.step = self.step
            ring.reset()

            for item in ring:
                item_str = "{},{},{}".format(item.name, item.age, item.gender)
                result_str += '{' + item_str + '}; '            
        
        else:
            result_str = 'No data input'
        
        return result_str