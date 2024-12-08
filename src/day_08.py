from src.day_04 import Coord
from collections import defaultdict

class Antenna(Coord):
    def __init__(self, x, y, value):
        super().__init__(x, y)
        self.value = value

def resonant_collinearity(file_list):
    antennas = []
    for y_idx, row in enumerate(file_list):
        for x_idx, char in enumerate(row):
            if char == ".":
                continue
            antennas.append(Antenna(x=x_idx, y=y_idx, value=char))

    grouped_antennas = defaultdict(list)
    for antenna in antennas:
        grouped_antennas[antenna.value].append(antenna)

    identified_coords = []

    for group in grouped_antennas.values():
        identified_coords.extend(get_antinodes(group)) 

    max_x = len(file_list[0]) - 1
    max_y = len(file_list) - 1

    valid_coords = remove_invalid_coords(identified_coords, max_x, max_y)
    set_coords = set(valid_coords)
    individual_items = len(set_coords)
    return individual_items

def get_antinodes(group):
    coords = []
    for antenna_coord in group:
        for other_coord in group:
            if antenna_coord == other_coord:
                continue
            coords.extend(get_opposite_coords(other_coord, antenna_coord))
    return coords

def get_opposite_coords(other_coord, antenna_coord):
    vector = Coord(antenna_coord.x-other_coord.x, antenna_coord.y-other_coord.y)
    first_coord = Coord(antenna_coord.x + vector.x, antenna_coord.y + vector.y)
    second_coord = Coord(other_coord.x-vector.x, other_coord.y-vector.y)

    return [first_coord,second_coord]

def remove_invalid_coords(identified_coords, max_x, max_y):
    return [coord for coord in identified_coords if 
            coord.x <= max_x 
            and coord.y <= max_y 
            and coord.x >= 0 
            and coord.y >= 0]

