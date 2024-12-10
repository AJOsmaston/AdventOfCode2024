from collections import deque

class Trails():
    def __init__(self, starting_coord, current_coord, score):
        self.starting_coord = starting_coord
        self.current_coord = current_coord
        self.score = score


def hoof_it(line_list):
    int_lists = [[int(char) for char in item] for item in line_list]
    starting_trail_list = get_starts(int_lists)
    finishes = 0
    for trail in starting_trail_list:
        dict, _ = breadth_first_search(int_lists, trail)
        finishes += len(dict.values())
    return finishes

def hoof_it_p2(line_list):
    int_lists = [[int(char) for char in item] for item in line_list]
    starting_trail_list = get_starts(int_lists)
    finishes = 0
    for trail in starting_trail_list:
        _, count = breadth_first_search(int_lists, trail)
        finishes += count
    return finishes

def get_starts(list_of_lists):
    starts = []
    y = 0
    for column in list_of_lists:
        x = 0
        for char in column:
            if char == 0:
                starts.append(Trails((x, y), (x, y), 0))
            x += 1
        y += 1
    return starts
            
def breadth_first_search(grid, start):
    print(start.starting_coord)
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = deque([start])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    finishes = {}
    count = 0

    while queue:
        this_trail = queue.popleft()
        x, y = this_trail.current_coord
        # if (x,y) in visited:
        #     continue

        visited.add((x,y))

        this_value = grid[y][x]

        for direction_x, direction_y in directions:
            x_dir_x, y_dir_y = x + direction_x, y + direction_y
            if 0 <= x_dir_x < cols and 0 <= y_dir_y < rows:
                if (x_dir_x, y_dir_y) in visited:
                    continue
                next_value = grid[y_dir_y][x_dir_x]
                if next_value - this_value == 1:
                    if next_value == 9:
                        this_trail.score += 1
                        this_trail.current_coord = (x_dir_x, y_dir_y)
                        finishes[this_trail.current_coord] = this_trail.starting_coord
                        print(f"Found a peak! Peak:{this_trail.current_coord}, steps:{this_trail.score}")
                        count +=1
                        continue
                    queue.append(Trails(this_trail.starting_coord, (x_dir_x, y_dir_y), this_trail.score + 1))
    
    return finishes, count
