from src.day_04 import Coord
from collections import defaultdict

class Antenna(Coord):
    def __init__(self, x, y, value):
        super().__init__(x, y)
        self.value = value

def resonant_collinearity(file_list):
    grouped_antennas = get_grouped_antennas(file_list)

    identified_coords = []

    max_x = len(file_list[0]) - 1
    max_y = len(file_list) - 1

    for group in grouped_antennas.values():
        identified_coords.extend(get_antinodes(group, max_x, max_y, get_opposite_coords)) 

    set_coords = set(identified_coords)
    individual_items = len(set_coords)
    return individual_items

def get_grouped_antennas(file_list):
    antennas = []
    for y_idx, row in enumerate(file_list):
        for x_idx, char in enumerate(row):
            if char == ".":
                continue
            antennas.append(Antenna(x=x_idx, y=y_idx, value=char))

    grouped_antennas = defaultdict(list)
    for antenna in antennas:
        grouped_antennas[antenna.value].append(antenna)
    return grouped_antennas

def resonant_collinearity_p2(file_list):
    grouped_antennas = get_grouped_antennas(file_list)

    identified_coords = []

    max_x = len(file_list[0]) - 1
    max_y = len(file_list) - 1

    for group in grouped_antennas.values():
        identified_coords.extend(get_antinodes(group, max_x, max_y, get_all_coords)) 

    set_coords = set(identified_coords)
    individual_items = len(set_coords)
    return individual_items

def get_antinodes(group, max_x, max_y, coord_function):
    coords = []
    for antenna_coord in group:
        for other_coord in group:
            if antenna_coord == other_coord:
                continue
            coords.extend(coord_function(other_coord, antenna_coord, max_x, max_y))
    return coords

def get_opposite_coords(other_coord, antenna_coord, max_x, max_y):
    vector = Coord(antenna_coord.x-other_coord.x, antenna_coord.y-other_coord.y)
    first_coord = Coord(antenna_coord.x + vector.x, antenna_coord.y + vector.y)
    second_coord = Coord(other_coord.x-vector.x, other_coord.y-vector.y)
    coords = [first_coord,second_coord]
    return [coord for coord in coords if coord.x <= max_x and coord.y <= max_y and coord.x >= 0 and coord.y >= 0]

def get_all_coords(other_coord, antenna_coord, max_x, max_y):
    vector = Coord(antenna_coord.x-other_coord.x, antenna_coord.y-other_coord.y)
    coords = []
    coords.append(Coord(antenna_coord.x,antenna_coord.y))
    coords.append(Coord(other_coord.x,other_coord.y))
    tracking_x = vector.x + antenna_coord.x
    tracking_y = vector.y + antenna_coord.y
    while(tracking_x <= max_x and tracking_x >= 0 and tracking_y <= max_y and tracking_y >= 0):
        coords.append(Coord(tracking_x, tracking_y))
        tracking_x += vector.x
        tracking_y += vector.y 
    tracking_x = other_coord.x-vector.x
    tracking_y = other_coord.y-vector.y
    while(tracking_x <= max_x and tracking_x >= 0 and tracking_y <= max_y and tracking_y >= 0):
        coords.append(Coord(tracking_x, tracking_y))
        tracking_x -= vector.x
        tracking_y -= vector.y
    return coords
