from file_helpers import file_helper
from src import day_11

file_data = file_helper.get_data("11", test=True)
actual_data = file_helper.get_data("11")

def test_day_11_p1_example_6():
    assert day_11.plutonian_pebbles(file_data, times=6) == 22

def test_day_11_p1_example_25():
    assert day_11.plutonian_pebbles(file_data, times=25) == 55312

def test_day_11_p1_actual():
    day_11_actual = day_11.plutonian_pebbles(actual_data, times=25)
    assert day_11_actual == 200446

def test_day_11_p2_actual():
    assert day_11.plutonian_pebbles(actual_data, times=75) == 238317474993392
