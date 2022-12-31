import random, json

NORTH = 0
SOUTH = 1
EAST = 2
WEST = 3
NORTHWEST = 4
SOUTHWEST = 5
NORTHEAST = 6
SOUTHEAST = 7
DOWN = 8
UP = 9

LATERAL_DIRECTIONS = [
NORTH,
SOUTH,
EAST,
WEST,
NORTHWEST,
SOUTHWEST,
NORTHEAST,
SOUTHEAST
]

OPPOSITE_DIRECTIONS = {
    NORTH: SOUTH,
    SOUTH: NORTH,
    EAST: WEST,
    WEST: EAST,
    NORTHWEST: SOUTHEAST,
    SOUTHWEST: NORTHEAST,
    NORTHEAST: SOUTHWEST,
    SOUTHEAST: NORTHEAST,
    DOWN: UP,
    UP: DOWN
}

DIRECTION_VECTOR = {
    NORTH : (1, 0, 0),
    SOUTH : (-1, 0, 0),
    EAST : (0, 0, 1),
    WEST : (0, 0, -1),
    NORTHWEST : (1, 0, -1),
    SOUTHWEST : (-1, 0, -1),
    NORTHEAST : (1, 0, 1),
    SOUTHEAST : (-1, 0, 1),
    DOWN: (0, -1, 0),
    UP: (0, 1, 0)
}

DOOR = "door"
PASSAGE = "passage"
LOCKED_DOOR = "locked door"
OBSTRUCTION = "obstruction"
SECRET_DOOR = "secret door"

class Dungeon:
    def __init__(self):
        self.rooms = {}

    def get_rooms_by_floor(self, floor):
        ret = []
        for room in self.rooms.values():
            if room.y == floor:
                ret.append(room)
        return ret

    def add_room(self, room):
        self.rooms[room.get_id()] = room

    def get_room_to_extend(self, floor):
        floor_rooms = self.get_rooms_by_floor(floor)
        if len(floor_rooms) == 0:
            return None
        random.shuffle(floor_rooms)
        for room in floor_rooms:
            empty_adjacencies = self.get_empty_adjacencies(room)
            if len(empty_adjacencies) > 0:
                return room
        return None

    def get_empty_adjacencies(self, room):
        empty_adjacencies = []
        adjacent_points = get_adjacent_points(room.get_point())
        for point in adjacent_points:
            key = format_point_key(point)
            if key not in self.rooms:
                empty_adjacencies.append(point)
        return empty_adjacencies

    # Adjacent means lateral. Ignores veritcal adjacencies
    def get_adjacent_rooms(self, point):
        adjacent_points = get_adjacent_points(point)
        rooms = []
        for point in adjacent_points:
            key = format_point_key(point)
            if key in self.rooms:
                rooms.append(self.rooms[key])
        return rooms

    def add_floor_room(self, floor):
        room = self.get_room_to_extend(floor)
        if room is None:
            room = Room(0, floor, 0)
        adjacencies = self.get_empty_adjacencies(room)
        point = random.choice(adjacencies)
        self.add_room(Room(point[0], point[1], point[2]))

    def draw_floor(self, floor):
        rooms = self.get_rooms_by_floor(floor)
        for room in rooms:
            pass
            #print(room.get_id())
        print(f"Rooms: {len(rooms)}")
        max_x = get_max_x(rooms)
        min_x = get_min_x(rooms)
        max_z = get_max_z(rooms)
        min_z = get_min_z(rooms)
        width = (max_x - min_x) + 1
        depth = (max_z - min_z) + 1
        #print(f"{max_x}, {min_x}, {max_z}, {min_z}")
        #print(f"{width}, {depth}")
        drw = f"LEVEL {floor}:\n"
        drw += "############\n"
        for i in range(-5, 5):
            drw += "#"
            for j in range(-5, 5):
                key = format_point_key((i, floor, j))
                #print(key)
                if key in self.rooms:
                    drw += "X"
                else:
                    drw += " "
            drw += "#"
            drw += "\n"
        drw += "############"
        return drw

def get_min_x(rooms):
    minimum = rooms[0].x
    for room in rooms:
        if minimum > room.x:
            minimum = room.x
    return minimum

def get_max_x(rooms):
    maximum = rooms[0].x
    for room in rooms:
        if maximum < room.x:
            maximum = room.x
    return maximum

def get_min_z(rooms):
    minimum = rooms[0].z
    for room in rooms:
        if minimum > room.z:
            minimum = room.z
    return minimum

def get_max_z(rooms):
    maximum = rooms[0].z
    for room in rooms:
        if maximum < room.z:
            maximum = room.z
    return maximum


class Room:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.connections = []

    def get_id(self):
        return format_point_key(self.get_point())

    def get_point(self):
        return (self.x, self.y, self.z)

    def __str__(self):
        return str(self.get_id())


class Connection:
    def __init__(self, direction, connection_type):
        self.direction = direction
        self.type = connection_type

def get_adjacent_points(point):
    points = []
    for direction in LATERAL_DIRECTIONS:
        points.append(move_direction(point, direction))
    return points

def move_direction(point, direction):
    vector = DIRECTION_VECTOR[direction]
    return (point[0] + vector[0], point[1] + vector[1], point[2] + vector[2])

def format_point_key(point):
    return f"[{point[0]},{point[1]},{point[2]}]"

def build_dungeon():
    dungeon = Dungeon()
    for i in range(6):
        for j in range(15):
            dungeon.add_floor_room(i)
    return dungeon


def main():
    dungeon = build_dungeon()
    for i in range(6):
        print(dungeon.draw_floor(i))

main()