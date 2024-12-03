from file_helpers import file_helper
from src.day_03 import mull_it_over, mull_it_over_p2

day3_test_data = file_helper.get_data(3, test=True)

def test_day_03_p1_example():
    assert mull_it_over(day3_test_data) == 161

def test_day_03_p2_example():
    assert mull_it_over_p2(day3_test_data) == 48

def test_day_02_p2_example_more_data():
    more_test_data = "+do()+do()+do()xmul(1,1)&mul[3,7]!^don't()_mul(5,5)-do()+mul(1,1)+do()(mul(1,1)undo()?mul(1,1))"
    assert mull_it_over_p2(more_test_data) == 4

day3_actual_data = file_helper.get_data(3)

def test_day_03_p1_actual():
    assert mull_it_over(day3_actual_data) == 173731097

def test_day_03_p2_actual():
    answer = mull_it_over_p2(day3_actual_data)
    assert answer != 417662989
    assert mull_it_over_p2(day3_actual_data) == 93729253
