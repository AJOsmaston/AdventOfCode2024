class TrackedIndex:
    def __init__(self, index):
        self.index = index

class EmptySpace:
    def __init__(self, start_index):
        self.start_index = start_index
        self.count = 1

def disk_fragmenter(file_text):
    file_freespace = get_files_with_freespace(file_text)
    first_empty_space = file_freespace.index([])
    for array, idx in zip(reversed(file_freespace), reversed(range(len(file_freespace)))):
        if first_empty_space >= idx:
            break
        if not array:
            continue
        for tracked_index in array:
            if first_empty_space == idx:
                file_freespace[first_empty_space].append(tracked_index)
                continue
            file_freespace[first_empty_space] = [tracked_index]
            first_empty_space = file_freespace.index([])
            
        del file_freespace[idx]

    return get_checksum(file_freespace)

def disk_fragmenter_p2(file_text):
    file_freespace = get_files_with_freespace(file_text)
    moved_files = move_files(file_freespace)
    return get_checksum(moved_files)

def get_files_with_freespace(file_text):
    file_freespace = []
    file=None
    for idx, char in enumerate(file_text):
        if file is None:
            file = char
            continue
        tracked_index = TrackedIndex(int((idx-1)/2))
        file_freespace.append([tracked_index for _ in range(int(file))])
        for i in range(int(char)):
            file_freespace.append([])
        file=None
        
    if file != None:
        file_freespace.append([TrackedIndex(tracked_index.index + 1) for _ in range(int(file))])
    return file_freespace

def get_checksum(file_freespace):
    total = 0
    index = 0
    for files in file_freespace:
        if files == []:
            index +=1
            continue
        for file in files:
            if file == []:
                index +=1
                continue
            total += (index * file.index)
            index += 1
    return total

def move_files(file_freespace):
    empty_spaces = get_empty_spaces(file_freespace)
    moved=[]
    for array, idx in zip(reversed(file_freespace), reversed(range(len(file_freespace)))):
        if not array:
            continue
        if array[0] in moved:
            continue
        for empty_space in empty_spaces:
            if empty_space.start_index >= idx:
                continue
            if len(array) > empty_space.count:
                continue
            for tracked_index in array:
                file_freespace[empty_space.start_index] = [tracked_index]
                empty_space.count-=1
                empty_space.start_index = empty_space.start_index + 1
                moved.append(tracked_index)
            file_freespace[idx] = [[] for _ in range(len(array))]
            break
    return file_freespace

def get_empty_spaces(file_freespace):
    empty_spaces = []
    this_empty_space = None
    for idx, file in enumerate(file_freespace):
        if file == []:
            if this_empty_space is None:
                this_empty_space = EmptySpace(idx)
                continue
            this_empty_space.count += 1
            continue
        if this_empty_space is None:
            continue
        empty_spaces.append(this_empty_space)
        this_empty_space = None
    return empty_spaces
        