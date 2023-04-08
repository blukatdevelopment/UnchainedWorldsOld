import json
from hex.cell import Cell

ALPHA_NUM = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25
}

TERRAIN = "Terrain"
HILLSIDE = "Hillside"
FOREST = "Forest"
DARKWOODS = "DarkWoods"
SWAMP = "Swamp"
DESERT = "Desert"
COASTAL_WATER = "Coastal Water"
OCEAN = "Ocean"
BAY = "Bay"
MOUNTAIN = "Mountain"
TERRAINS = [HILLSIDE, FOREST, DARKWOODS, SWAMP, DESERT, COASTAL_WATER, OCEAN, BAY, MOUNTAIN]
TERRAIN_COLORS = {
    HILLSIDE: (115, 222, 73),
    FOREST: (29, 84, 7),
    DARKWOODS: (15, 48, 2),
    SWAMP: (27, 54, 40),
    DESERT: (255, 234, 148),
    COASTAL_WATER: (59, 185, 255),
    OCEAN: (9, 79, 102),
    BAY: (144, 197, 214),
    MOUNTAIN: (255, 255, 255)
}



def load_json(path):
    with open(path, 'r') as file:
        json_obj = file.read()
        return json.loads(json_obj)

def load_hexes():
    return load_json('./hex/hexes.json')

def name_to_coords(name):
    x = int(name[1:])
    y_alpha = name[0:1]
    y = ALPHA_NUM[y_alpha]
    return (x, y)

def load_cells():
    hexes = load_hexes()
    cells = []
    for hx in hexes:
        coords = name_to_coords(hx["name"])
        color = TERRAIN_COLORS[hx[TERRAIN]]
        #print(f"Color: {color}, coords: {coords}")
        cell = Cell(hx["name"], color, coords, hx[TERRAIN])
        cells.append(cell)

    return cells