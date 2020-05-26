import os,sys
sys.path.append("C:\\Users\\76747\\Desktop\\Python\\practice\\Josephus")

from domain.user_interface.iu_curses import CursesWindow
from domain.shared import person as bc
from domain.adapter.readers import readers as rds
from domain.use_cases import josephus as jsp
from domain.user_interface.process_data_and_output import ProcessDataAndOutput

if __name__ == '__main__':
    win = CursesWindow()
    win.set_win()
    people_text = win.create_input_str_area('data of people(separate with:";")', 0, 1, 100, 5)
    path = win.create_input_str_area('path', 0, 7, 100, 2).strip()
    file_name = win.create_input_str_area('file_name', 0, 10, 100, 2).strip()

    process = ProcessDataAndOutput()
    process.people_text = people_text
    process.path = path
    process.file_name = file_name

    try:
        start = int(win.create_input_str_area('start(int)', 0, 13, 100, 2).strip())
        step = int(win.create_input_str_area('step(int)', 0, 16, 100, 2).strip())
        process.start = start
        process.step = step
    except ValueError as e:
        raise ValueError('Start and step must be integer!')

    result_str = process.output_result_str()

    win.display_info("The result is:\n{}".format(result_str), 0, 20)
    win.display_info('Press any key to continue...',0 , 29)
    
    win.get_ch_and_continue()
    win.unset_win()
