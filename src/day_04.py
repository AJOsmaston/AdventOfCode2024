class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other): 
        if not isinstance(other, Coord):
            return NotImplemented
        return self.x == other.x and self.y == other.y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __hash__(self):
        return hash(str(self))

def ceres_search_part_one(line_data):
    count = 0
    yCoord= 0
    for line in line_data:
        xCoord = 0
        for char in line:
            if char == "X":
                x = Coord(xCoord, yCoord)
                surrounding_ms = get_surrounding("M", line_data, x)  
                for m in surrounding_ms:
                    try:
                        vectorX = m.x - x.x
                        vectorY = m.y - x.y
                        aXcoord = m.x + vectorX
                        aYcoord = m.y + vectorY
                        if aYcoord < 0 or aXcoord < 0:
                            continue
                        if line_data[aYcoord][aXcoord] == "A":
                            sXcoord = m.x + vectorX + vectorX
                            sYcoord = m.y + vectorY + vectorY
                            if sXcoord < 0 or sYcoord < 0:
                                continue
                            if line_data[sYcoord][sXcoord] == "S":
                                count += 1
                    except Exception:
                        continue

            xCoord += 1
        yCoord += 1
    return count

def ceres_search_part_two(line_data):
    count = 0
    yCoord= 0
    for line in line_data:
        xCoord = 0
        for char in line:
            if char == "A":
                a = Coord(xCoord, yCoord)
                if a.x == 0 or a.y == 0 or a.x > len(line) or a.y > len(line_data):
                    xCoord += 1
                    continue
                surrounding_ms = get_surrounding("M", line_data, a)
                if len(surrounding_ms) < 2:
                    xCoord += 1
                    continue
                surrounding_ss = get_surrounding("S", line_data, a)
                if len(surrounding_ss) < 2:
                    xCoord += 1
                    continue

                top_left = Coord(a.x-1, a.y-1)
                top_right = Coord(a.x+1, a.y-1)
                bottom_left = Coord(a.x-1, a.y+1)
                bottom_right = Coord(a.x+1, a.y+1)
                opposites = {
                    top_left:bottom_right,
                    top_right:bottom_left,
                    bottom_right:top_left,
                    bottom_left:top_right
                }
                valid_coord = [top_left, top_right, bottom_left, bottom_right]

                for ms in surrounding_ms:
                    if ms in valid_coord:
                       if opposites[ms] in surrounding_ss:
                           valid_coord.remove(opposites[ms])
                           valid_coord.remove(ms)
                for ss in surrounding_ss:
                    if ss in valid_coord:
                        if opposites[ss] in surrounding_ms:
                           valid_coord.remove(opposites[ss])
                           valid_coord.remove(ss)

                if len(valid_coord) == 0:
                    count += 1
            xCoord += 1
            
        yCoord += 1
    return count

def get_surrounding(letter, line_data, coord):
    surrounding = []
    try_append(surrounding, line_data, coord.x-1, coord.y, letter)
    try_append(surrounding, line_data, coord.x-1, coord.y+1, letter)
    try_append(surrounding, line_data, coord.x-1, coord.y-1, letter)
    try_append(surrounding, line_data, coord.x, coord.y-1, letter)
    try_append(surrounding, line_data, coord.x, coord.y+1, letter)
    try_append(surrounding, line_data, coord.x+1, coord.y-1, letter)
    try_append(surrounding, line_data, coord.x+1, coord.y, letter)
    try_append(surrounding, line_data, coord.x+1, coord.y+1, letter)
    return surrounding

def try_append(list, line_data, xcoord, ycoord, letter):
    if ycoord < 0 or xcoord < 0:
        return
    try:
        if line_data[ycoord][xcoord] == letter:
            list.append(Coord(xcoord, ycoord))
    except Exception as e:
        return
