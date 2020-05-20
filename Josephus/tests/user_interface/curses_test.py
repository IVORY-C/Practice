import os,sys
sys.path.append("C:\\Users\\76747\\Desktop\\Python\\practice\\Josephus")

from main.shared import base_class as bc
from main.adapter import readers as rds
from main.use_cases import josephus as jsp

import curses
from curses.textpad import Textbox, rectangle
from typing import List

stdscr = curses.initscr()

def display_info(info, x, y, colorpair=2):
    global stdscr
    stdscr.addstr(y, x, info, curses.color_pair(colorpair))
    stdscr.refresh()

def get_ch_and_continue():
    global stdscr
    stdscr.nodelay(0)
    ch = stdscr.getch()
    stdscr.nodelay(1)
    return True

def set_win():
    global stdscr
    curses.start_color()

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    curses.noecho()
    curses.cbreak()
    stdscr.nodelay(1)

def unset_win():
    global stdstr
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()

def create_input_str_area(stdscr, input_note: str, start_x: int, start_y: int, size_x: int, size_y: int) -> str:
    stdscr.addstr(start_y, start_x, f"Enter {input_note}: (hit Ctrl-G to send)")

    editwin = curses.newwin(size_y, size_x, start_y+1, start_x+1)
    stdscr.refresh()

    box = Textbox(editwin, insert_mode=True)
    box.edit()
    info = box.gather()
    return info

if __name__ == '__main__':
    set_win()
    people_text = create_input_str_area(stdscr, 'data(separate with:";")', 0, 1, 100, 5)
    path = create_input_str_area(stdscr, 'path', 0, 7, 100, 2).strip()
    file_name = create_input_str_area(stdscr, 'file_name', 0, 10, 100, 2).strip()
    try:
        start = int(create_input_str_area(stdscr, 'start(int)', 0, 13, 100, 2).strip())
        step = int(create_input_str_area(stdscr, 'step(int)', 0, 16, 100, 2).strip())
    except ValueError as e:
        raise ValueError('Start and step must be integer!')

    reader = []
    result_str = ''
    if people_text:
        people_str: List[str] = people_text.split(';')
        for each in people_str:
            if not each:
                continue 
            data = each.replace(' ','').strip().split(',')
            name: str = data[0]
            try:
                age = int(data[1])
            except:
                age = -1
            gender: str = data[2]
            reader.append(bc.Person(name, age, gender))

    if path:
        try:
            file_type = file_name.split('.')[1]

            if file_type == 'txt':
                file_reader = rds.TxtReader(path)
            if file_type == 'csv':
                file_reader = rds.CsvReader(path)
            if file_type == 'zip':
                file_reader = rds.ZipReader(path, file_name)

                reader = file_reader.create_person_from_file()
        except ValueError as e:
            raise ValueError('Input incorrect path or file_name!')

    if reader:
        ring = jsp.Ring(reader)
        ring.start = start
        ring.step = step
        ring.reset()

        for item in ring:
            item_str = f"{item.name},{item.age},{item.gender}"
            result_str += "{" + item_str + '}; '            
    
    else:
        result_str = 'No data input'

    stdscr.addstr(20, 0, f"The result is:\n{result_str}")
    display_info('Press any key to continue...',0,29)
    
    get_ch_and_continue()
    unset_win()
