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

NORTH = "north"
SOUTH = "south"
EAST = "east"
WEST = "west"

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
    print("Set {} to {}".format(setting, config[setting]))
  else:
    print("Setting missing: {}".format(setting))

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
      return "{}->{}".format(self.a_id, self.b_id)

class Object(object):
    pass


def build_dungeon():
  dun = Dungeon()
  for i in range(len(config[FLOOR])):
    floor = config[FLOOR][i]
    level = i + 1
    rooms = floor[ROOMS]
    print("Building floor {} with {} rooms".format(level, rooms))
    init_level(dun, level, rooms)

def init_level(dun, level, room_count):
  connections = 
  rooms = []
  unassigned = []
  for i in range(room_count):
    room = Room()
    room.z = level
    rooms.add(room)
    unassigned.add[i]

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

    # Connect it to current room
    conn = Connection()
    conn.first_id = current_room.get_id()
    current_direction = random.choice([NORTH, EAST, WEST, SOUTH])
    while current_direction == last_direction;
      current_direction = random.choice([NORTH, EAST, WEST, SOUTH])

    match current_direction:
    case NORTH:
         next_room.y += 1
         conn.second_id
    case EAST:
         next_room.x += 1
    case WEST:
         next_room.x -= 1
    case SOUTH:
        next_room.y -= 1
    conn.second_id = next_room.get_id()

def get_next_empty_coord(current_room, rooms):
  found = False
  while not found:
    new_x = current_room.x
    new_y = current_room.y
    # Pick from eight cardinal and diagonal directions
    direction = random.choice([1, 2, 3, 4, 5, 6, 7, 8])
    match direction:
    case 1:
      new_x -= 1
      new_y += 1
      pass
    case 2:
      new_y += 1
      pass
    case 3:
      new_x += 1
      new_y += 1
      pass
    case 4:
      new_x -= 1
      pass
    case 5:
      new_x += 1
      pass
    case 6:
      new_x -= 1
      new_y -= 1
      pass
    case 7:
      new_y -= 1
      pass
    case 8:
      new_x += 1
      new_y -= 1
      pass
    if not room_exists():
      found = true
  return (new_x, new_y)

def room_exists(x, y, z, rooms):
  for room in rooms:
    if room.x == x and room.y == y and room.z == z:
      return True
    return False
# main
def main():
  read_config()
  build_config_objects()
  dungeon = build_dungeon()

main()