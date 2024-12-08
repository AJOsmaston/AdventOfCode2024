from file_helpers import file_helper
from src import day_02


file_data = file_helper.get_line_list_from_data("2", test=True)
actual_data = file_helper.get_line_list_from_data("2")

def test_day_02_p1_example():
    assert day_02.RedNosedReports(file_data) == 2

def test_day_02_p1_actual():
    assert day_02.RedNosedReports(actual_data) == 639

def test_day_02_p2_example():
    assert day_02.RnRp2(file_data) == 4

def test_day_02_p2_actual():
    assert day_02.RnRp2(actual_data) == 674
