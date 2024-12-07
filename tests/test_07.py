from file_helpers.file_helper import get_line_list_from_data
from src.day_07 import bridge_repair_p1, bridge_repair_p2

example_file_dat_list = get_line_list_from_data(7, test=True)

def test_day_05_p1_example():
    assert bridge_repair_p1(example_file_dat_list) == 3749

def test_day_05_p2_example():
    assert bridge_repair_p2(example_file_dat_list) == 11387

actual_file_data_list = get_line_list_from_data(7)

def test_day_05_p1_actual():
    day_04_p1 = bridge_repair_p1(actual_file_data_list)
    assert day_04_p1 == 12940396350192

def test_day_05_p2_actual():
    day_04_p2 = bridge_repair_p2(actual_file_data_list)
    assert day_04_p2 == 106016735664498