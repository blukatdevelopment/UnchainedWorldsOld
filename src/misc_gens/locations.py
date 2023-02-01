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

WATER_SOURCES = [
"creek",
"creek",
"creek",
"creek",
"stream",
"stream",
"stream",
"stream",
"well",
"well",
"well",
"well",
"white water rapids",
"waterfall",
"river",
"pond",
"hotsprings",
"geyser",
"lake"]

NATRUAL_RESOURCES = [
    "bee hives",
    "fungal field",
    "leathery lichens",
    "nests of fist-sized glowbugs",
    "moledog tunnels",
    "berry field",
    "honey ant mound",
    "fluffy tree forest",
    "wild game forest",
    "abandoned orchard",
    "abandoned wheat farm",
    "floating coral reef",
    "giant leech spawning pool"
]

RELIGIOUS_FIGURES = ["Bimros",
"Gegtex",
"Kord",
"Uaos",
"Exheia",
"Gidur",
"Solus",
"Coent",
"Coenta",
"Coento",
"Titan King: Batchek",
"Titan King: Tihomir",
"Titan King: Petrov",
"Titan King: Balcaen",
"Titan King: Yavor",
"Titan King: Toncheh",
"J'ra, unrequainted prince",
"Famine",
"Magara, the hoard god",
"Tuzzazz, the slumberer",
"Kirr, rage queen",
"Fusch the face stealer",
"Grokug and Porok, the conquerer twins",
"Zimzin, the walker king",
"Nekatur, the seducer",
"Docla, starvation devil",
"Barnoth, fashion devil",
"Brenzen, dream devil",
"Korrath, Reaper of War",
"Pientara, the gossip king",
"Wro Gentar, devil of bodies",
"Bestlar Mranag"]

SITE_STRUCTURES = [
"shrine",
"temple",
"statue",
"graveyard",
"altar"
]

AGES = [
"Divine Age",
"Age of Dragons",
"Titan Age",
"Empire of man",
"Post-Severing"
]

SITE_CONDITION = [
"abandoned",
"poorly maintained",
"well maintained",
"pristeen"
]

WONDROUS_ANOMALIES = [
"bottomless pit",
"fey rock circle",
"fey mushroom circle",
"fey river gate",
"fey fountain",
"fey statues",
"sentient wishing well",
"talking tree(cursed person)",
"gate to ethereal plane, active at twilight",
"500ft tall stone pillar",
"statue of man with sword",
"dragon skeleton",
"giant skull",
"pool of corrupting liquid",
"pool of lava",
"wild magic zone",
"anti-magic zone",
"weak magic zone",
"zero gravity zone",
"double gravity zone",
"half time zone",
"double time zone",
"magical darkness zone",
"magical twilight zone",
"abyssal energy zone",
"undeath energy zone",
"always raining zone",
"never raining zone",
"icy cold zone",
"brutally hot zone",
"always foggy zone",
"haunted woodlands",
"+1 sword in a stone(must have 20STR to pull out)",
"talking statues",
"battlefield of petrified warriors",
"primordial 14 laws miniature monolith",
"an inland sailboat",
"20ft tall sculpture of a hand",
"imp trade shop",
"awakening zone(creatures become awakened inside)",
"animation zone(objects become animated inside)",
"reanimation zone(the dead are immediately raised as zombies)",
"radiant zone (1d6 radiant damage per minute)",
"tiny folk community in a bridge",
"tiny folk community in a clock tower",
"crater with meteorite in center",
"haunted battlefield",
"ethereal-merged spirit zone",
"portal to hell",
"magic circle on platform",
"field of annihilation",
"acid rain zone",
"powerful winds zone"
]

ARTIFACTS = [
"Titan armor",
"wheeled transport",
"air transport",
"tank",
"artillery vehicle",
"train",
"airship",
"forgeling scrapyard",
"space probe",
"giant forgeling soldier"]

RUINS_BUILDINGS = [
"house",
"farmstead",
"village",
"town",
"city",
"clocktower",
"drawbridge",
"fort",
"keep"
"castle",
"stadium",
"watch tower",
"courthouse",
"inn",
"tavern",
"shop",
"cabin",
"office building",
"parking garage",
"forgeling factory",
"hospital",
"movie theater",
"shopping mall"
]

DEN_MONSTERS = [
"Tentacle Beast",
"Pincer Beast",
"Wolf bat",
"Stone Scurrier",
"Giant Ant",
"Sha Karr",
"Mind Leech",
"Flesh Eaters",
"Chaos Shells",
"Infernoids",
"Mantis Man",
"Leech Man",
"Sentinel",
"Floating Eye",
"Giant Hand",
"Spindle Man",
"Muckbeast",
"Needlenose",
"Chameleoid",
"Raystalker",
"Manface silkworm",
"Marionette spider",
"Invisible Skulker",
"Changeling",
"Land Urchin",
"Carpet Worm",
"Swarm of Heart Worms",
"Pit Fisher",
"Mimic",
"Hydra",
"Zombie",
"Skeletons",
"Shadow",
"Ghost / Banshee / Specter",
"Breath Skull",
"Skelemancer",
"Vampire",
"Slime(Any)",
"Rotheads",
"Grass Heap",
"Root Walkers",
"Fey Guardian",
"Shroom People",
"Nymph",
"Arch Fey",
"Giant Crab",
"Snarl Beak",
"Huge Polar Bear",
"Sharp Tooth",
"Saber-toothed Tiger",
"Dire Wolf",
"Giant Spider",
"Brown Bear",
"Mountain Lion",
"Giant Leech",
"Featherclaws",
"Littlefoot",
"Sand Guardian",
"Flame Guardian",
"Grinders",
"Abyssal Giant",
"Bone Thresher",
"Gattogat",
"Vice",
"Imp",
"Regret",
"Devil Scribes",
"Hell Knight",
"Hell Hounds",
"Bandit(any)",
"Soldier (any)",
"Cultists(Any)",
"Dwarf Giants"
]


def worship_site():
    condition = random.choice(SITE_CONDITION)
    figure = random.choice(RELIGIOUS_FIGURES)
    age = random.choice(AGES)
    structure = random.choice(SITE_STRUCTURES)
    return f"{condition} {structure} of {figure} from the {age}"

def artifact():
    return random.choice(ARTIFACTS)

def ruins():
    return random.choice(RUINS_BUILDINGS)

def natural_resource(terrain):
    if terrain not in [HILLSIDE, FOREST]:
        return ""
    return random.choice(NATRUAL_RESOURCES)

def wondrous_anomaly():
    return random.choice(WONDROUS_ANOMALIES)

def natural_anomaly():
    first = random.choice([
        "boulder",
        "crevasse",
        "crater",
        "sinkhole",
        "mud pit",
        "hill",
        "termite mound",
        "tree",
        "caravan wreck",
        "pile of bones",
        "series of boulders",
        "tiny lake",
        "space devoid of plants",
        "grey soil",
        "plume of thick vegetation",
        "thornpatch",
        "collapsed tunnel",
        "shallow cave",
        "acid lake",
        "brackish pond",
        "surface deposit of iron",
        "surface deposit of copper",
        "surface deposit of salt",
        "surface deposit of fossils",
        ])
    second = random.choice([
        "bone",
        "skull and crossbones",
        "heart",
        "smile",
        "frown",
        "watchglass",
        "the monolith of Bimros",
        "sword",
        "dagger",
        "volumetric flask",
        "dog",
        "cat",
        "pawprint",
        "ghost",
        "arrow",
        "bird",
        "symbol of Gidur",
        "circle",
        "square",
        "plus sign",
        "rectangle",
        "triangle",
        "X"
        ])
    return f"{first} resembling a(n) {second}"

def den():
    return random.choice(DEN_MONSTERS) + " den"

def water_source(terrain):
    if terrain in [COASTAL_WATER, OCEAN, BAY]:
        return ""
    elif terrain == HILLSIDE and random.randint(1, 4) == 1:
        return ""
    elif terrain in [FOREST, DARKWOODS, MOUNTAIN] and random.randint(1, 2) == 1:
        return ""
    elif terrain == DESERT and random.randint(1, 4) > 1:
        return ""
    elif terrain == SWAMP:
        return "swamp water"
    return random.choice(WATER_SOURCES)

def generate_locations(terrain):
    locations = []
    resource = natural_resource(terrain)
    if resource != "":
        locations.append(resource)
    if random.randint(1, 20) == 1:
        locations.append(wondrous_anomaly())
    water = water_source(terrain)
    locations.append(den())
    locations.append(natural_anomaly())
    locations.append(worship_site())
    locations.append(wondrous_anomaly())

    random.shuffle(locations)
    if water != "":
        locations.insert(0, water)
    return locations

def fill_hex(hx):
    locations = generate_locations(hx[TERRAIN])
    if hx["1"] == "":
        hx["1"] = locations.pop(0)
    if hx["2"] == "":
        hx["2"] = locations.pop(0)
    if hx["3"] == "":
        hx["3"] = locations.pop(0)
    return hx

def get_hexes():
    hexes = []
    with open("hexes.json", 'r') as file:
        data = file.read()
        hexes = json.loads(data)

    return hexes

def test():
    print(natural_anomaly())
    print(worship_site())
    print(artifact())
    print(ruins())
    print(wondrous_anomaly())
    print(den())
    for terrain in TERRAINS:
        print(terrain)
        print(natural_resource(terrain))
        print(water_source(terrain))
        print(generate_locations(terrain))

def main():
    hexes = get_hexes()
    filled_hexes = []

    for hx in hexes:
        filled_hexes.append(fill_hex(hx))
    print(json.dumps(filled_hexes, indent=4))
    pass

main()
#test()