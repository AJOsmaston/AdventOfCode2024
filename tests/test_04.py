from file_helpers.file_helper import get_line_list_from_data
from src.day_04 import ceres_search_part_one, ceres_search_part_two

example_file_data = get_line_list_from_data(4, test=True)

def test_day_04_p1_example():
    assert ceres_search_part_one(example_file_data) == 18

def test_day_04_p2_example():
    assert ceres_search_part_two(example_file_data) == 9

actual_file_data = get_line_list_from_data(4)

def test_day_04_p1_actual():
    day_04_p1 = ceres_search_part_one(actual_file_data)
    assert day_04_p1 == 2560

def test_day_04_p2_actual():
    day_04_p2 = ceres_search_part_two(actual_file_data)
    assert day_04_p2 == 1910