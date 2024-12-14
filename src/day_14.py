from PIL import Image
import os

class Robot:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        
    @classmethod
    def from_string(cls, data):
        components = data.split()
        position = None
        velocity = None
        
        for component in components:
            if component.startswith("p="):
                positions = component[2:].split(',')
                position = Coord(int(positions[0]), int(positions[1]))
            elif component.startswith("v="):
                velocities = component[2:].split(',')
                velocity = Coord(int(velocities[0]), int(velocities[1]))
        
        return cls(position, velocity)
    
class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def restroom_redoubt(file_lines, max_x, max_y):
    quadrants = {
        1:[],
        2:[],
        3:[],
        4:[]
    }
    for line in file_lines:
        robot = Robot.from_string(line)
        end_position = move_robot_with_turns(robot, max_x, max_y, 100)
        quadrant = determine_quadrant(end_position, max_x, max_y)
        if quadrant == 0:
            continue
        quadrants[quadrant].append(end_position)
    
    safety_factor = get_safety_factor(quadrants)
    return safety_factor

def move_robot_with_turns(robot, max_x, max_y, turns):
    while turns > 0:
        move_robot(robot, max_x, max_y)
        turns -= 1
    return robot.position

def move_robot(robot, max_x, max_y):
    robot.position.x += robot.velocity.x
    
    if robot.position.x >= max_x:
        robot.position.x -= max_x
    if robot.position.x < 0:
        robot.position.x += max_x
    robot.position.y += robot.velocity.y
    if robot.position.y >= max_y:
        robot.position.y -= max_y
    if robot.position.y < 0:
        robot.position.y += max_y
    
def determine_quadrant(end_position, max_x, max_y):
    end_x = end_position.x
    end_y = end_position.y
    mid_x = (max_x-1)/2
    mid_y = (max_y-1)/2
    #quadrant 1 == top left
    if end_x < mid_x and end_y < mid_y:
        return 1
    #quad 2 == top right
    if end_x > mid_x and end_y < mid_y:
        return 2
    #quad 3 == bottom left
    if end_x < mid_x and end_y > mid_y:
        return 3
    #quad 4 == bottom right
    if end_x > mid_x and end_y > mid_y:
        return 4
    return 0

def get_safety_factor(quadrants):
    total = 1
    for list in quadrants.values():
        total *= len(list)
    return total

def restroom_redoubt_tree_hunt(file_lines, times):
    max_x = 101
    max_y = 103
    count = 0
    robots = []
    for line in file_lines:
            robots.append(Robot.from_string(line))

    while times > 0:
        count += 1
        file_number = "{:06d}".format(count)
        file_location = os.path.join(os.getcwd(), "bitmaps", f"{file_number}_tree.bmp")
        end_positions = []
        for robot in robots:
            end_positions.append(move_robot_with_turns(robot, max_x, max_y, 1))
        generate_bitmap(end_positions, max_x, max_y, file_location)
        times -= 1

def generate_bitmap(coords, max_x, max_y, output_file):
    img = Image.new("RGB", (max_x, max_y), "white")
    pixels = img.load()
    
    for coord in coords:
        if 0 <= coord.x < max_x and 0 <= coord.y < max_y:
            pixels[coord.x, coord.y] = (0, 0, 0)  # Black
    
    img.save(output_file)
