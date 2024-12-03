import re

class Mul:
    def __init__(self, left_value, right_value):
        self.left_value=left_value
        self.right_value=right_value

    def calculate_mul(self):
        return self.left_value * self.right_value

def mull_it_over(file_string):
    #extract potential muls
    muls = extract_muls(file_string)

    total_sum = 0
    #execute function
    for mul in muls:
        total_sum += mul.calculate_mul()

    #sum total
    return total_sum

def mull_it_over_p2(file_string):
    do_pattern = re.escape("do()")
    dont_pattern = re.escape("don't()")
    start_indexes = [m.start() for m in re.finditer(do_pattern, file_string)]
    end_indexes = [m.start() for m in re.finditer(dont_pattern, file_string)]
    start_indexes.insert(0, 0)
    end_indexes.append(len(file_string))

    substrings = generate_substrings(start_indexes, end_indexes, file_string)

    mul_sums = 0
    for substring in substrings:
        mul_sums += mull_it_over(substring)

    return mul_sums

def generate_substrings(start_flags, stop_flags, input_string):
    if len(stop_flags) == 0:
        return [input_string]
    current_index = 0

    substrings = []

    while current_index < len(input_string):
        for start_flag in start_flags:
            if start_flag >= current_index:
                start_index = start_flag
                current_index = start_flag
                break
        for stop_flag in stop_flags:
            if stop_flag > start_index and stop_flag > current_index:
                stop_index = stop_flag
                current_index = stop_flag
                break
        substrings.append(input_string[start_index:stop_index])    

    return substrings

def extract_muls(file_string):
    index_array = [m.start() for m in re.finditer('mul', file_string)]
    # mul(123,456)
    mul_max_length = 12
    potential_muls = [file_string[index:(index+mul_max_length)] for index in index_array]
    final_muls = []
    for mul in potential_muls:
        valid_mul = get_valid(mul)
        if valid_mul != None:
            final_muls.append(valid_mul)
    return final_muls

def get_valid(mul):
    start_bracket_idx = mul.find('(')
    if start_bracket_idx != 3:
        return None
    end_bracket_idx = mul.find(')')
    if end_bracket_idx == -1 or end_bracket_idx <= (start_bracket_idx + 1):
        return None
    
    brackets_substring = mul[(start_bracket_idx + 1):(end_bracket_idx)]
    numbers_list = brackets_substring.split(',')
    if len(numbers_list) != 2:
        return None
    
    try:
        first_int = int(numbers_list[0])
        second_int = int(numbers_list[1])
    except Exception as e:
        print(e)
        return None

    return Mul(first_int, second_int)
    
def calculate_mul(mul):
    pass
