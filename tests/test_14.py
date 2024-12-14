from file_helpers import file_helper
from src import day_14

file_data = file_helper.get_line_list_from_data("14", test=True)
actual_data = file_helper.get_line_list_from_data("14")

def test_day_14_p1_example():
    assert day_14.restroom_redoubt(file_data, max_x=11, max_y=7) == 12

def test_day_14_p1_actual():
    day_14_actual = day_14.restroom_redoubt(actual_data, max_x=101, max_y=103)
    assert day_14_actual == 217132650

#running this will generate 15000 images. I wouldn't advise running this.
#def test_not_really_a_test():
#    day_14.restroom_redoubt_tree_hunt(file_lines=actual_data, times=15000)
