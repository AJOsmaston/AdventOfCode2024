import os

def get_line_list_from_data(day, test=False):
    if len(str(day)) == 1:
        day = "0" + str(day)
    
    actual_string = "actual"
    test_string = "example"

    file_name = f"{day}_{test_string}.txt" if test else f"{day}_{actual_string}.txt"
    file_path = os.path.join(os.getcwd(), "data", file_name)

    with open(file_path) as file:
        return file.read().split("\n")
