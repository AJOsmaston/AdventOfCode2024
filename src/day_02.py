def RedNosedReports(file_data):
    reports = file_data.split("\n")

    total_safe = 0
    for report in reports:
        total_safe += is_report_safe(report)

    return total_safe

def RnRp2(file_data):
    reports = file_data.split("\n")

    total_safe = 0
    for report in reports:
        base_safe = is_report_safe(report)
        total_safe += base_safe
        if base_safe:
            continue

        total_safe += is_report_safeish(report)

    return total_safe

def is_report_safe(report):
    items_in_report = report.split(" ")
    is_decreasing = False
    is_increasing = False
    safe_change = 3
    previous_item = None

    for item in items_in_report:
        int_item = int(item)
        if not previous_item:
            previous_item = int_item
            continue

        if int_item == previous_item:
            return False
        if int_item > previous_item:
            is_increasing = True
        if int_item < previous_item:
            is_decreasing = True

        if is_decreasing and is_increasing:
            return False
        
        difference = abs(int_item - previous_item)
        if difference > safe_change:
            return False
        previous_item = int_item
    return True

def is_report_safeish(report):
    for index, _ in enumerate(report.split(" ")):
        new_report = report.split(" ")
        new_report.pop(index)
        if is_report_safe(" ".join(new_report)):
            return True
    return False
