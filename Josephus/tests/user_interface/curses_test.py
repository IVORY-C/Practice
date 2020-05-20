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

def input_str(stdscr, input_note: str, start_x: int, start_y: int, size_x: int, size_y: int):
    stdscr.addstr(start_y, start_x, f"Enter {input_note}: (hit Ctrl-G to send)")

    editwin = curses.newwin(size_y, size_x, start_y+1, start_x+1)
    stdscr.refresh()

    box = Textbox(editwin, insert_mode=True)
    box.edit()
    info = box.gather()
    return info

if __name__ == '__main__':
    try:
        set_win()
        people_text = input_str(stdscr, 'data', 0, 1, 100, 5)
        path = input_str(stdscr, 'path', 0, 7, 100, 2).strip()
        file_name = input_str(stdscr, 'file_name', 0, 10, 100, 2).strip()
        start = input_str(stdscr, 'start', 0, 13, 100, 2).strip()
        step = input_str(stdscr, 'step', 0, 16, 100, 2).strip()

        reader = []
        if people_text:
            people_str: List[str] = people_text.split('\n')
            for each in people_str:
                if not each:
                    continue 
                data: List[str] = each.split(',')
                name = data[0]
                age = int(data[1])
                gender = data[2]
                reader.append(bc.Person(name, age, gender))

        if path:
            file_type = file_name.split('.')[1]
            if file_type == 'txt':
                file_reader = rds.TxtReader(path)
            if file_type == 'csv':
                file_reader = rds.CsvReader(path)
            if file_type == 'zip':
                file_reader = rds.ZipReader(path, file_name)

            reader = file_reader.create_person_from_file()

        if reader:
            ring = jsp.Ring(reader)
            ring.start = int(start)
            ring.step = int(step)
            ring.reset()

            result_str = ''
            for item in ring:
                item_str = f"{item.name},{item.age},{item.gender}"
                result_str += item_str + '\n'            
        
        else:
            result_str = 'No data input'

        stdscr.addstr(30, 0, result_str)
        # display_info('Press any key to continue...',0,34)
        get_ch_and_continue()
    except Exception as e:
        raise e
    finally:
        unset_win()
