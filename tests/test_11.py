from file_helpers import file_helper
from src import day_11

file_data = file_helper.get_data("11", test=True)
# actual_data = file_helper.get_data("11")

def test_day_11_p1_example_6():
    assert day_11.plutonian_pebbles(file_data, times=6) == 22

def test_day_11_p1_example_25():
    assert day_11.plutonian_pebbles(file_data, times=25) == 55312

# def test_day_11_p1_actual():
#     day_08_actual = day_11.plutonian_pebbles(actual_data)
#     assert day_08_actual == 0

# def test_day_11_p2_example():
#     assert day_11.plutonian_pebbles_p2(file_data) == 0

# def test_day_11_p2_actual():
#     assert day_11.plutonian_pebbles_p2(actual_data) == 0
