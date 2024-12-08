import file_helpers.file_helper as file_helper
import src.day_01 as day_01


file_data = file_helper.get_line_list_from_data("1", test=True)

def test_day_01_p1_example():
    assert day_01.Historian_Hysteria(file_data) == 11

def test_day_01_p2_example():
    assert day_01.part_two(file_data) == 31

actual_file_data = file_helper.get_line_list_from_data("1")

def test_day_01_p1_actual():
    assert day_01.Historian_Hysteria(actual_file_data) == 2086478

def test_day_01_p2_actual():
    assert day_01.part_two(actual_file_data) == 24941624
