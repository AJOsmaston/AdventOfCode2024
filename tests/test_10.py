from file_helpers import file_helper
from src import day_10

file_data = file_helper.get_line_list_from_data("10", test=True)
actual_data = file_helper.get_line_list_from_data("10")

def test_day_10_p1_example():
    assert day_10.hoof_it(file_data) == 36

def test_day_10_p1_actual():
    day_08_actual = day_10.hoof_it(actual_data)
    assert day_08_actual == 489

def test_day_10_p2_example():
    assert day_10.hoof_it_p2(file_data) == 81

def test_day_10_p2_actual():
    assert day_10.hoof_it_p2(actual_data) == 1086
