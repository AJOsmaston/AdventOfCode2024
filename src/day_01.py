def Historian_Hysteria(file_data):
    leftlist, rightlist = get_both_lists(file_data)

    leftlist.sort()
    rightlist.sort()

    zipped = zip(leftlist, rightlist)
    sum = 0
    for zipa, zipb in zipped:
        diff = abs(zipa - zipb)
        sum += diff
    return sum
    
def part_two(file_data):
    leftlist, rightlist = get_both_lists(file_data)
    individual_items = set(leftlist)
    freq = {}
    for item in individual_items:
        freq[item] = rightlist.count(item)

    sum = 0
    for item in leftlist:
        sum += freq[item] * item
    return sum

def get_both_lists(line_pairs):
    leftlist = []
    rightlist = []
    for line in line_pairs:
        lrdata = line.split(" ")
        left = int(lrdata[0].strip())
        right = int(lrdata[-1].strip())
        leftlist.append(left)
        rightlist.append(right)
    return leftlist, rightlist