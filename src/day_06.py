from src.day_04 import Coord
import copy

class Guard:
    def __init__(self, position, image):
        self.position = position
        self.image = image
        self.vector

    @property
    def vector(self):
        guard_vectors = {
            "^" : [0 , -1],
            ">" : [1 , 0],
            "V" : [0 ,+1],
            "<" : [-1, 0]
        }
        return guard_vectors[self.image]

guard_chars = ["^", ">", "V", "<"]

def guard_gallivant_p1(file_list):
    guard, block_coords = setup_initial_board(file_list, guard_chars)
    visited_coords = travel(guard, file_list, block_coords, guard_chars)
    return len(set(visited_coords.keys()))

def guard_gallivant_p2(file_list):
    pass

def setup_initial_board(file_list, guard_chars):
    block_coords = []
    guard = None
    for y_idx, row in enumerate(file_list):
        for x_idx, char in enumerate(row):
            if char == ".":
                continue
            if char == "#":
                block_coords.append(Coord(x_idx, y_idx))
            if char in guard_chars:
                guard = Guard(Coord(x_idx, y_idx), char)
    return guard, block_coords

def travel(guard, file_list, block_coords, guard_chars):
    max_x = len(file_list[0]) - 1
    max_y = len(file_list) - 1
    coord_dict = {}
    while guard.position.x < max_x and guard.position.y < max_y and guard.position.x >= 0 and guard.position.y >= 0:
        move_guard_forward(guard)
        if guard.position in block_coords:
            move_guard_forward(guard, reverse=True)
            guard.image = get_next_image(guard.image, guard_chars)
            continue
        coord = Coord(guard.position.x, guard.position.y)
        if coord not in coord_dict:
            coord_dict[coord] = [guard.image]
        else:
            this_image_list = coord_dict[coord]
            if guard.image in this_image_list:
                raise Exception()
            else:
                coord_dict[coord].append(guard.image)
    return coord_dict

def get_next_image(direction, directions):
    index = directions.index(direction) 
    next_index = (index + 1) % len(directions)
    return directions[next_index]

def move_guard_forward(guard, reverse=False):
    unit = 1
    if reverse:
        unit = -1

    if guard.vector == [0 , 1]:
        guard.position.y += unit
    elif guard.vector == [1 , 0]:
        guard.position.x += unit
    elif guard.vector == [0 ,-1]:
        guard.position.y -= unit
    elif guard.vector == [-1, 0]:
        guard.position.x -= unit