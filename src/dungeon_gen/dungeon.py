#!/usr/bin/python3

# This script generates a markdown file containing a skeletal dungeon.
# The intention is that the generated file will be finished by hand.

import random

# Constants
DUNGEON_NAME = "dungeon_name"
TOTAL_GP = "total_gp"
TOTAL_ENEMY_XP = "total_enemy_xp"
SECRET_ROOMS = "secret_rooms"

# Entities
FLOOR = "floor"
ENEMY = "enemy"
LOOT = "loot"
SCENERY = "scenery"
TRAP = "trap"
ENTITY_MAX = 5

# Entity properties
ROOMS = "rooms"
LEVEL = "level"
NAME = "name"
XP = "xp"
GP = "gp"

# Connection end types
DOOR = "door"
PASSAGE = "passage"
LOCKED_DOOR = "locked door"
OBSTRUCTION = "obstruction"
SECRET_DOOR = "secret door"

NORTH = "North"
SOUTH = "South"
EAST = "East"
WEST = "West"
NORTHWEST = "NorthWest"
SOUTHWEST = "SouthWest"
NORTHEAST = "NorthEast"
SOUTHEAST = "SouthEast"

# Raw text settings and also objects
config = {}

def read_config():
  for line in open("config.txt"):
    parse_setting(line)

def parse_setting(line):
  line = line.replace('\n', '')
  if not line or line == '\n' or line[0] == '#':
    #print("Skipping blank or commented line")
    return
  
  parts = line.split("=")
  if len(parts) < 2:
    #print("Empty setting: '{}'".format(line))
    return
  setting = parts[0]
  setting_value = parts[1]
  config[setting] = setting_value
  #print("Added setting for {} as {}".format(setting, setting_value))

def build_config_objects():
  build_general_settings()
  build_entity_list(FLOOR,[ROOMS])
  build_entity_list(ENEMY,[NAME, XP])
  build_entity_list(LOOT,[NAME, GP])
  build_entity_list(SCENERY,[NAME])
  build_entity_list(TRAP,[NAME])

def build_general_settings():
  settings = [DUNGEON_NAME, TOTAL_GP, TOTAL_ENEMY_XP, SECRET_ROOMS]
  setting_types = ["str", "int", "int", "int"]
  for i in range(len(settings)):
    build_setting(settings[i], setting_types[i])

def build_setting(setting, setting_type):
  if setting in config:
    if setting_type == "int":
      val = config[setting]
      val = int(val) if val.isdecimal() else None
      if val is None:
        print("Setting must be whole number: " + setting)
        return
      
      config[setting] = val
    else:
      config[setting] = config[setting]
    #print("Set {} to {}".format(setting, config[setting]))
  #else:
    #print("Setting missing: {}".format(setting))

def build_entity_list(entity_name, properties):
  config[entity_name] = []
  for i in range(ENTITY_MAX):
    entity = {}
    prop_missing = False
    for prop in properties:
      prop_key = "{}_{}_{}".format(entity_name, i, prop)
      if prop_key in config:
        entity[prop] = config[prop_key]
      else:
        prop_missing = True
        #print("prop missing: {}".format(prop_key))
    if not prop_missing:
      config[entity_name].append(entity)
      #print("{} {} inserted: {}".format(entity_name, i, entity))
    else:
      pass
      #print("{} {} missing properties".format(entity_name, i))


class Dungeon:
    def __init__(self):
      self.rooms = {}
      self.connections = []

class Room:
    def __init__(self):
      self.x = 0
      self.y = 0
      self.z = 0
      self.secret = False
      self.scenery = []
      self.enemies = []
      self.connections = []

    def get_id(self):
      return "[{},{},{}]".format(self.x, self.y, self.z)

class Connection:
    def __init__(self):
      self.first_id = ""
      self.second_id = ""
      self.first_type = ""
      self.second_type = ""
      self.first_dir = ""
      self.second_dir = ""

    def get_id(self):
      return "{}->{}".format(self.first_id, self.second_id)

class Object(object):
    pass

#------------------------------------------------------------------------------#
# Dungeon building
#------------------------------------------------------------------------------#

def build_dungeon():
  dun = Dungeon()
  for i in range(len(config[FLOOR])):
    floor = config[FLOOR][i]
    level = i + 1
    room_count = floor[ROOMS]
    init_level(dun, level, room_count)
  return dun

def init_level(dungeon, level, room_count):
  #print("init_level({}, {}, {})".format(dungeon, level, room_count))
  # Create rooms
  rooms = []
  unassigned = []
  for i in range(int(room_count)):
    room = Room()
    room.z = level
    rooms.append(room)
    unassigned.append(i)
  if len(rooms) == 0:
    return

  # Place rooms
  current_room = rooms[0]
  last_direction = ""
  current_direction = ""
  while len(unassigned) > 0:
    # Get the next room
    next_id = unassigned[0]
    unassigned.remove(next_id)
    next_room = rooms[next_id]
    next_room.x = current_room.x
    next_room.y = current_room.y

    # Place it nearby
    coords = get_next_empty_coord(current_room, rooms)
    if coords is None:
      print("Oh, gee, it finally happened! :(")
      return
    next_room.x = coords[0]
    next_room.y = coords[1]
    current_room = next_room

  for room in rooms:
    dungeon.rooms[room.get_id()] = room
    #print("Room at coords {}".format(room.get_id()))
  connect_level(dungeon, rooms)

  

def get_next_empty_coord(current_room, rooms):
  found = False
  iterations = 0
  new_x = current_room.x
  new_y = current_room.y
  while not found:
    iterations += 1  
    # Pick from eight cardinal and diagonal directions
    direction = random.choice([1, 2, 3, 4])
    match direction:
      case 1:
        new_x += 1
      case 2:
        new_x -= 1
      case 3:
        new_y += 1
      case 4:
        new_y -= 1
    if not room_exists(new_x, new_y, current_room.z, rooms):
      found = True
    elif iterations > 100:
      return None
  #print("Does not exist yet [{},{},{}]".format(new_x, new_y, current_room.z))
  #for room in rooms:
  #  print(room.get_id())
  return (new_x, new_y)

def room_exists(x, y, z, rooms):
  for room in rooms:
    if room.x == x and room.y == y and room.z == z:
      return True
    #print("Room [{},{},{}] does not exist yet".format(x, y, z))
  return False

def print_dungeon_level(dungeon, level):
  rooms = get_rooms_by_level(list(dungeon.rooms.values()), level)
  out = "Dungeon level {}\n".format(level)
  for y in range(-15, 15, 1):
    for x in range(-15, 15, 1):
      if get_room_by_coords(x, y, level, rooms) is not None:
        out += "R"
      else:
        out += " "
    out += "\n"
  print(out)

def get_room_by_coords(x, y, z, rooms):
  for room in rooms:
    if room.x == x and room.y == y and room.z == z:
      return room
  #print("no room at [{}, {}, {}]".format(x, y, z))
  return None

def get_room_by_id(id, rooms):
  for room in rooms:
    if room.get_id() == id:
      return room
  return None

def get_rooms_by_level(rooms, level):
  #print("Rooms: {}".format(len(rooms)))
  level_rooms = []
  for room in rooms:
    #print("Comparing {} to {}".format(level, room.z))
    if room.z == level:
      level_rooms.append(room)
  return level_rooms

def connect_level(dungeon, rooms):
  conn_strings = {}
  for room in rooms:
    for neighbor in get_neighbors(room, rooms):
      connection = "{}->{}".format(room.get_id(), neighbor.get_id())
      reverse_connection = "{}->{}".format(neighbor.get_id(), room.get_id())
      if connection not in conn_strings and reverse_connection not in conn_strings:
        conn_strings[connection] = True
  for conn_string in conn_strings:
    conn = Connection()
    parts = conn_string.split('->')
    conn.first_id = parts[0]
    conn.second_id = parts[1]
    conn.first_type = PASSAGE
    conn.second_type = PASSAGE
    conn.first_dir = NORTH
    conn.second_dir = SOUTH
    dungeon.connections.append(conn)

# Check for neighbors on the same level
def get_neighbors(room, rooms):
  neighbors = []
  for candidate in rooms:
    x_dist = abs(candidate.x - room.x)
    y_dist = abs(candidate.y - room.y)
    if room is not candidate and x_dist < 2 and y_dist < 2:
      neighbors.append(candidate)
  return neighbors
# main
def main():
  read_config()
  build_config_objects()
  dungeon = build_dungeon()
  for i in [1, 2]:
    print_dungeon_level(dungeon, i)
  for conn in dungeon.connections:
    print(conn.get_id())


def main2():
  rooms = []
  room1 = Room()
  room1.x = 1
  room1.y = 1
  room1.z = 1
  rooms.append(room1)

  if not room_exists(1, 1, 1, rooms):
    print("Room doesn't exist")
  else:
    print("Room does exist")

main()