import os,sys
sys.path.append("C:\\Users\\76747\\Desktop\\Python\\practice\\Josephus")

from domain.user_interface.iu_curses import CursesWindow
from domain.shared import person as bc
from domain.adapter.readers import readers as rds
from domain.use_cases import josephus as jsp

if __name__ == '__main__':
    win = CursesWindow()
    win.set_win()
    people_text = win.create_input_str_area('data of people(separate with:";")', 0, 1, 100, 5)
    path = win.create_input_str_area('path', 0, 7, 100, 2).strip()
    file_name = win.create_input_str_area('file_name', 0, 10, 100, 2).strip()
    try:
        start = int(win.create_input_str_area('start(int)', 0, 13, 100, 2).strip())
        step = int(win.create_input_str_area('step(int)', 0, 16, 100, 2).strip())
    except ValueError as e:
        raise ValueError('Start and step must be integer!')

    reader = []
    result_str = ''

    if people_text and path:
        raise ValueError('Cannot input both people and file path!')

    if people_text and not path:
        try:
            people_str = people_text.split(';')
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
                reader.append(bc.Person(name, age, gender))
        except:
            raise ValueError('Input incorrect data of people!')

    if path and not people_text:
        try:
            file_type = path.split('.')[-1]

            if file_type == 'txt':
                file_reader = rds.TxtReader(path)
            if file_type == 'csv':
                file_reader = rds.CsvReader(path)
            if file_type == 'zip':
                file_reader = rds.ZipReader(path, file_name)

            reader = file_reader.create_person_from_file()
        except:
            raise ValueError('Input incorrect path or file_name!')

    if reader:
        ring = jsp.Ring(reader)
        ring.start = start
        ring.step = step
        ring.reset()

        for item in ring:
            item_str = "{},{},{}".format(item.name, item.age, item.gender)
            result_str += '{' + item_str + '}; '            
    
    else:
        result_str = 'No data input'

    win.display_info("The result is:\n{}".format(result_str), 0, 20)
    win.display_info('Press any key to continue...',0 , 29)
    
    win.get_ch_and_continue()
    win.unset_win()
