from file_helpers import file_helper
from src import day_08

file_data = file_helper.get_line_list_from_data("8", test=True)
actual_data = file_helper.get_line_list_from_data("8")

def test_08_example():
    assert day_08.resonant_collinearity(file_data) == 14

def test_08_actual():
    day_08_actual = day_08.resonant_collinearity(actual_data)
    assert  day_08_actual < 413
    assert day_08_actual == 409

# def test_08b_example():
#     assert day_08.RnRp2(file_data) == 4

# def test_08b_actual():
#     assert day_08.RnRp2(actual_data) == 674
