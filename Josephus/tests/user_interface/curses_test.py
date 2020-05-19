from main.shared import base_class as bc
from main.adapter import readers as rds
from main.use_cases import josephus as jsp

import curses
from curses.textpad import Textbox, rectangle

stdscr = curses.initscr()

def display_info(info, x, y, colorpair=2):
    global stdscr
    stdscr.addstr(y, x, info, curses.color_pair(colorpair))
    stdscr.refresh()

def get_ch_and_continue():
    global stdscr
    stdscr.nodelay(0)
    ch=stdscr.getch()
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

def input_str(stdscr, input_note: str):
    stdscr.addstr(0, 0, f"Enter {input_note}: (hit Ctrl-G to send)")

    editwin = curses.newwin(2,1, 5,30)
    rectangle(stdscr, 1,0, 1+5+1, 1+30+1)
    stdscr.refresh()

    box = Textbox(editwin)
    box.edit()
    data = box.gather()

    return data


def test_func():
    try:
        set_win()
        data = input_str(stdscr, 'data')

        people = []
        for each in self._all_data:
            data = each.strip().replace(' ','').split(',')
            name = data[0]
            try:
                age = int(data[1])
            except ValueError as e:
                age = -2
            gender = data[2]
            people.append(bc.Person(name, age, gender))
        
        ring = jsp.Ring(people)
        ring.reset()
        ring.start = 2
        ring.step = 5
        
        result_str = ''
        for item in ring:
            data_someone = line.split(',')
            data_someone_str = f"Name: {data[0]}, Age: {data[1]}, Gender: {data[2]}"
            result += data_str + '\n'

        display_info(result,0,10)
        display_info('Press any key to continue...',0,20)
        get_ch_and_continue()
    except Exception as e:
        raise e
    finally:
        unset_win()
