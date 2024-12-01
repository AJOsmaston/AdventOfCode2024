import file_helpers.file_helper as file_helper
import src.day_01 as day_01


file_data = file_helper.get_data("1", test=True)

def test_01_example():
    assert day_01.Historian_Hysteria(file_data) == 11

def test_02_example():
    assert day_01.part_two(file_data) == 31

actual_file_data = file_helper.get_data("1")

def test_01_actual():
    assert day_01.Historian_Hysteria(actual_file_data) == 2086478

def test_02_actual():
    assert day_01.part_two(actual_file_data) == 24941624
