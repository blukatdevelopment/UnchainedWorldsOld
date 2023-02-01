#!/usr/bin/python3
import random, json
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

TERRAIN = "Terrain"
NAME = "name"

ALPHA = [
"A",
"B",
"C",
"D",
"E",
"F",
"G",
"H",
"I",
"J",
"K",
"L",
"M",
"N"
]

NUMERIC = 12


def generate_hexes():
    hexes = []
    for alpha in ALPHA:
        for i in range(NUMERIC):
            name = f"{alpha}{i}"
            hexes.append(gen_hex(name))
    print(json.dumps(hexes, indent=1))

def gen_hex(name):
    hx = {}
    hx[NAME] = name
    hx[TERRAIN] = ""
    hx["1"] = ""
    hx["2"] = ""
    hx["3"] = ""
    return hx

def count_hexes(filename):
    data = ""
    with open(filename, 'r') as file:
        data = file.read()
    hexes = json.loads(data)
    print(f"There are {len(hexes)} hexes.")
    regions = {}
    regions[HILLSIDE] = []
    regions[FOREST] = []
    regions[DARKWOODS] = []
    regions[SWAMP] = []
    regions[DESERT] = []
    regions[COASTAL_WATER] = []
    regions[OCEAN] = []
    regions[BAY] = []
    regions[MOUNTAIN] = []


    for hx in hexes:
        terrain = hx[TERRAIN]
        regions[terrain].append(hx[NAME])
    for terrain in TERRAINS:
        region = regions[terrain]
        print(f"There are {len(region)} {terrain} hexes.")
        print(json.dumps(region))

def main():
    count_hexes("hexes.json")

main()