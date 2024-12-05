from file_helpers.file_helper import get_line_list_from_data
from src.day_05 import print_queue_p1, print_queue_p2

example_file_dat_list = get_line_list_from_data(5, test=True)

def test_day_05_p1_example():
    assert print_queue_p1(example_file_dat_list) == 143

def test_day_05_p2_example():
    assert print_queue_p2(example_file_dat_list) == 123

actual_file_data = get_line_list_from_data(5)

def test_day_05_p1_actual():
    day_04_p1 = print_queue_p1(actual_file_data)
    assert day_04_p1 == 4281

def test_day_05_p2_actual():
    day_04_p2 = print_queue_p2(actual_file_data)
    assert day_04_p2 == 5466