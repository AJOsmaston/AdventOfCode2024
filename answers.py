import file_helpers.file_helper as file_helper
import src.day_01 as day_01


day1_data = file_helper.get_data(1)
print("Q1:")
print(day_01.Historian_Hysteria(day1_data))
print("Q1b:")
print(day_01.part_two(day1_data))
