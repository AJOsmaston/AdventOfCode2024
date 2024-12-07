class Rule:
    def __init__(self, string_input):
        split_input = string_input.split("|")
        small_item = int(split_input[0])
        large_item = int(split_input[1])
        self.first_item = small_item
        self.second_item = large_item

    def __eq__(self, other): 
        if not isinstance(other, Rule):
            return NotImplemented
        return self.first_item == other.first_item and self.second_item == other.second_item
    
    def __str__(self):
        return f"{self.first_item}>{self.second_item}"
    def __hash__(self):
        return hash(str(self))

def print_queue_p1(file_list):
    rules, manuals = get_rules_and_manuals(file_list)

    success_manuals = [manual for manual in manuals if is_success(manual, rules)]

    return get_total_middles(success_manuals)

def print_queue_p2(file_text):
    rules, manuals = get_rules_and_manuals(file_text)

    fixed_manuals = []
    for manual in manuals:
        all_rules_set, comparison_dict = get_rule_sets_with_dict(manual, rules)
        if not(check_rules(all_rules_set, comparison_dict)):
            fixed_manuals.append(fix_manual(all_rules_set, comparison_dict))

    return get_total_middles(fixed_manuals)

def fix_manual(all_rules_set, comparison_dict):
    counter = 0
    all_rules = list(all_rules_set)
    while counter < len(all_rules):
        rule = all_rules[counter]
        try:
            smaller_item = comparison_dict[rule.first_item]
            larger_item = comparison_dict[rule.second_item]
            if smaller_item > larger_item:
                counter = 0
                comparison_dict[rule.first_item] = larger_item
                comparison_dict[rule.second_item] = smaller_item
                continue
        except:
            counter += 1
            continue
        counter += 1
    return [key for key, _ in sorted(comparison_dict.items(), key=lambda item: item[1])]

def get_total_middles(success_manuals):
    total_middles = 0
    for success_manual in success_manuals:
        length=len(success_manual)
        middle_string = success_manual[int((length - 1) / 2)]
        total_middles += int(middle_string)
    return total_middles

def is_success(manual, rules):
    all_rules_set, comparison_dict = get_rule_sets_with_dict(manual, rules)
    return check_rules(all_rules_set, comparison_dict)

def check_rules(all_rules_set, comparison_dict):
    for rule in all_rules_set:
        try:
            smaller_item = comparison_dict[rule.first_item]
            larger_item = comparison_dict[rule.second_item]
            if smaller_item > larger_item:
                return False
        except:
            continue
    return True

def get_rule_sets_with_dict(manual, rules):
    comparison_dict = {}
    all_applicable_rules = []

    for idx, number in enumerate(manual):
        int_number = int(number)
        comparison_dict[int_number] = idx
        all_applicable_rules.extend(find_applicable_rules(rules, int(number)))

    all_rules_set = set(all_applicable_rules)
    return all_rules_set, comparison_dict

def find_applicable_rules(rules, number):
    return [rule for rule in rules if rule.first_item == number or rule.second_item == number]

def get_rules_and_manuals(file_list):
    rules = []
    manuals = []

    for line in file_list:
        if "|" in line:
            rules.append(Rule(line))
        if "," in line:
            manuals.append(line.split(","))

    return rules, manuals
