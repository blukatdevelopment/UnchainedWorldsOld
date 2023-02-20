#!/usr/bin/python3
import random, json

POPULATION = "population"
LOCATIONS = "locations"
NAME = "name"
POP_MIN = 80
POP_MAX = 2000
HEX = "hex"

NAMES = [
"Heinberg",
"Ironbend",
"Tinderheart",
"Redswell",
"Dullworth",
"Bingle",
"Sharleaf",
"Hoaryhog",
"Unleven",
"Darsaven",
"Brambleturn",
"Sevensteel",
"Vandenbert",
"Harf",
"Hiegal",
"Greyfield",
"Fireshant",
"Eagleton",
"Mintberg",
"Cloverfield",
"Blackfurnace",
"Mayfield",
"Rupertsville",
"Dinangle",
"Dunfield",
"Burberg",
"Shartruce",
"Indego",
"Goldleaf"
]

BASIC_LOCATIONS = [
"Tavern",
"Trapper",
"Cobbler",
"Open Market",
"Granary",
"Shrine",
"Bakery",
"Beekeepers",
"Herbalist"
]
MID_LOCATIONS = [
"Inn",
"Pub",
"Stables",
"Blacksmith",
"Tailor",
"Butcher",
"Workshop",
"General Store"
]
FANCY_LOCATIONS = [
"Apothecary",
"Healer",
"Spa",
"Tinkerer",
"School",
"Temple",
"Bathhouse",
"Mayor's House",
"Book Seller",
"Coach service"
]


def generate_village(name):
    village = {}
    village[NAME] = name
    village[HEX]=""
    village[POPULATION] = random.randint(POP_MIN, POP_MAX)
    village[LOCATIONS] = []
    basic = 0
    mid = 0
    fancy = 0
    if village[POPULATION] < 200:
        basic = 3
    elif village[POPULATION] < 500:
        basic = 3
        mid = 1
    elif village[POPULATION] < 750:
        basic = 3
        mid = 2
    elif village[POPULATION] < 1000:
        basic = 3
        mid = 3
        fancy = 1
    elif village[POPULATION] < 1500:
        basic = 3
        mid = 3
        fancy = 2
    elif village[POPULATION] < 2000:
        basic = 3
        mid = 3
        fancy = 3
    for i in range(basic):
        while True:
            location = random.choice(BASIC_LOCATIONS)
            if location not in village[LOCATIONS]:
                village[LOCATIONS].append(location)
                break
    for i in range(mid):
        while True:
            location = random.choice(MID_LOCATIONS)
            if location not in village[LOCATIONS]:
                village[LOCATIONS].append(location)
                break
    for i in range(fancy):
        while True:
            location = random.choice(FANCY_LOCATIONS)
            if location not in village[LOCATIONS]:
                village[LOCATIONS].append(location)
                break
    return village

def output_village(village):
    print(json.dumps(village, indent=1))

def main():
    for name in NAMES:
        village = generate_village(name)
        output_village(village)

main()