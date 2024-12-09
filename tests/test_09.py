from file_helpers import file_helper
from src import day_09

file_data = file_helper.get_data("9", test=True)
actual_data = file_helper.get_data("9")

def test_day_09_p1_example():
    assert day_09.disk_fragmenter(file_data) == 1928

# 3.7s
# def test_day_09_p1_actual():
#     day_08_actual = day_09.disk_fragmenter(actual_data)
#     assert day_08_actual > 90840102756
#     assert day_08_actual == 6395800119709

def test_day_09_p2_example():
    assert day_09.disk_fragmenter_p2(file_data) == 2858

# 7.03s
# def test_day_09_p2_actual():
#     assert day_09.disk_fragmenter_p2(actual_data) == 0
