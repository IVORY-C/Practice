from domain.shared import person as bc
from domain.adapter.readers import readers as rds
from domain.use_cases import josephus as jsp

import curses
from curses.textpad import Textbox, rectangle
from typing import List

class CursesWindow():
    def __init__(self):
        self.stdscr = curses.initscr()

    def display_info(self, info, x, y, colorpair=2):
        self.stdscr.addstr(y, x, info, curses.color_pair(colorpair))
        self.stdscr.refresh()

    def get_ch_and_continue(self):
        self.stdscr.nodelay(0)
        key = self.stdscr.getch()
        self.stdscr.nodelay(1)
        return True

    def set_win(self):
        curses.start_color()

        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

        curses.noecho()
        curses.cbreak()
        self.stdscr.nodelay(1)

    def unset_win(self):
        curses.nocbreak()
        self.stdscr.keypad(0)
        curses.echo()
        curses.endwin()

    def create_input_str_area(self, input_note: str, start_x: int, start_y: int, size_x: int, size_y: int) -> str:
        self.stdscr.addstr(start_y, start_x, f"Enter {input_note}: (hit Ctrl-G to send)")

        editwin = curses.newwin(size_y, size_x, start_y+1, start_x+1)
        self.stdscr.refresh()

        box = Textbox(editwin, insert_mode=True)
        box.edit()
        info = box.gather()
        return info

