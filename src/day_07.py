def bridge_repair_p1(input_list, part2=False):
    total = 0
    for row in input_list:
        split_row = row.split(':')
        test_value = int(split_row[0])
        remaining_numbers = split_row[1].strip().split(" ")
        if can_we_make_the_test_value(test_value, remaining_numbers, part2):
            total += test_value
    return total

def can_we_make_the_test_value(test_value, remaining_numbers, part2):
    sums = []
    for current_number in remaining_numbers:
        current_int = int(current_number)
        if not sums:
            sums.append(current_int)
            continue
        sums = get_next_sums(test_value, sums, current_int, part2)
    return test_value in sums

def get_next_sums(test_value, sums, current_number, part2):
    next_sums = []
    for sum in sums:
        multiply = sum * current_number
        add = sum + current_number
        if multiply <= test_value:
            next_sums.append(multiply)
        if add <= test_value:
            next_sums.append(add)
        if part2:
            combine = str(sum) + str(current_number)
            if int(combine) <= test_value:
                next_sums.append(int(combine))
    return next_sums     

def bridge_repair_p2(input_list):
    return bridge_repair_p1(input_list, True)