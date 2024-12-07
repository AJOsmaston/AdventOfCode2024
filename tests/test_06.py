from file_helpers.file_helper import get_line_list_from_data
from src.day_06 import guard_gallivant_p1, guard_gallivant_p2

example_file_dat_list = get_line_list_from_data(6, test=True)

def test_day_06_p1_example():
    assert guard_gallivant_p1(example_file_dat_list) == 41

#>0.5s
# def test_day_06_p2_example():
#     assert guard_gallivant_p2(example_file_dat_list) == 6

actual_file_data = get_line_list_from_data(6)

def test_day_06_p1_actual():
    day_04_p1 = guard_gallivant_p1(actual_file_data)
    assert day_04_p1 == 4711

#very very slow
# def test_day_06_p2_actual():
#     day_04_p2 = guard_gallivant_p2(actual_file_data)
#     assert day_04_p2 == 1562