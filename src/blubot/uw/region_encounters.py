import random

UNBROKEN_MOUNTAIN = "the Unbroken Mountains"
GIANTS_PLAYGROUND = "the Giant's Playground"
MOURNING_FOREST = "the Mourning Forest"
BLIGHTLANDS = "the Blightlands"
SENTINEL_WOODS = "the Sentinel Woods"
SCARS = "the Scars"
NORTH_OMARIA = "North Omaria"
MAJOR_ROADS = "major roads"
WATER = "water"

HEX_REGION_MAP = {
"A0": UNBROKEN_MOUNTAIN,
"A1": UNBROKEN_MOUNTAIN,
"A2": UNBROKEN_MOUNTAIN,
"A3": UNBROKEN_MOUNTAIN,
"A4": NORTH_OMARIA,
"A5": NORTH_OMARIA,
"A6": NORTH_OMARIA,
"A7": NORTH_OMARIA,
"A8": WATER,
"A9": WATER,
"A10": WATER,
"A11": WATER,
"B0": UNBROKEN_MOUNTAIN,
"B1": UNBROKEN_MOUNTAIN,
"B2": UNBROKEN_MOUNTAIN,
"B3": UNBROKEN_MOUNTAIN,
"B4": NORTH_OMARIA,
"B5": NORTH_OMARIA,
"B6": NORTH_OMARIA,
"B7": NORTH_OMARIA,
"B8": NORTH_OMARIA,
"B9": NORTH_OMARIA,
"B10": WATER,
"B11": WATER,
"C0": UNBROKEN_MOUNTAIN,
"C1": UNBROKEN_MOUNTAIN,
"C2": UNBROKEN_MOUNTAIN,
"C3": NORTH_OMARIA,
"C4": NORTH_OMARIA,
"C5": NORTH_OMARIA,
"C6": NORTH_OMARIA,
"C7": NORTH_OMARIA,
"C8": NORTH_OMARIA,
"C9": NORTH_OMARIA,
"C10": WATER,
"C11": WATER,
"D0": UNBROKEN_MOUNTAIN,
"D1": UNBROKEN_MOUNTAIN,
"D2": GIANTS_PLAYGROUND,
"D3": GIANTS_PLAYGROUND,
"D4": GIANTS_PLAYGROUND,
"D5": GIANTS_PLAYGROUND,
"D6": GIANTS_PLAYGROUND,
"D7": NORTH_OMARIA,
"D8": NORTH_OMARIA,
"D9": NORTH_OMARIA,
"D10": NORTH_OMARIA,
"D11": WATER,
"E0": GIANTS_PLAYGROUND,
"E1": GIANTS_PLAYGROUND,
"E2": GIANTS_PLAYGROUND,
"E3": GIANTS_PLAYGROUND,
"E4": GIANTS_PLAYGROUND,
"E5": GIANTS_PLAYGROUND,
"E6": GIANTS_PLAYGROUND,
"E7": NORTH_OMARIA,
"E8": NORTH_OMARIA,
"E9": NORTH_OMARIA,
"E10": WATER,
"E11": WATER,
"F0": GIANTS_PLAYGROUND,
"F1": GIANTS_PLAYGROUND,
"F2": GIANTS_PLAYGROUND,
"F3": GIANTS_PLAYGROUND,
"F4": GIANTS_PLAYGROUND,
"F5": GIANTS_PLAYGROUND,
"F6": GIANTS_PLAYGROUND,
"F7": GIANTS_PLAYGROUND,
"F8": NORTH_OMARIA,
"F9": NORTH_OMARIA,
"F10": WATER,
"F11": WATER,
"G0": GIANTS_PLAYGROUND,
"G1": GIANTS_PLAYGROUND,
"G2": GIANTS_PLAYGROUND,
"G3": GIANTS_PLAYGROUND,
"G4": GIANTS_PLAYGROUND,
"G5": GIANTS_PLAYGROUND,
"G6": GIANTS_PLAYGROUND,
"G7": NORTH_OMARIA,
"G8": NORTH_OMARIA,
"G9": WATER,
"G10": GIANTS_PLAYGROUND,
"G11": WATER,
"H0": MOURNING_FOREST,
"H1": GIANTS_PLAYGROUND,
"H2": GIANTS_PLAYGROUND,
"H3": GIANTS_PLAYGROUND,
"H4": GIANTS_PLAYGROUND,
"H5": GIANTS_PLAYGROUND,
"H6": GIANTS_PLAYGROUND,
"H7": GIANTS_PLAYGROUND,
"H8": GIANTS_PLAYGROUND,
"H9": GIANTS_PLAYGROUND,
"H10": GIANTS_PLAYGROUND,
"H11": GIANTS_PLAYGROUND,
"I0": MOURNING_FOREST,
"I1": MOURNING_FOREST,
"I2": GIANTS_PLAYGROUND,
"I3": GIANTS_PLAYGROUND,
"I4": GIANTS_PLAYGROUND,
"I5": GIANTS_PLAYGROUND,
"I6": GIANTS_PLAYGROUND,
"I7": GIANTS_PLAYGROUND,
"I8": GIANTS_PLAYGROUND,
"I9": GIANTS_PLAYGROUND,
"I10": GIANTS_PLAYGROUND,
"I11": GIANTS_PLAYGROUND,
"J0": MOURNING_FOREST,
"J1": MOURNING_FOREST,
"J2": GIANTS_PLAYGROUND,
"J3": GIANTS_PLAYGROUND,
"J4": GIANTS_PLAYGROUND,
"J5": GIANTS_PLAYGROUND,
"J6": GIANTS_PLAYGROUND,
"J7": GIANTS_PLAYGROUND,
"J8": GIANTS_PLAYGROUND,
"J9": GIANTS_PLAYGROUND,
"J10": GIANTS_PLAYGROUND,
"J11": GIANTS_PLAYGROUND,
"K0": MOURNING_FOREST,
"K1": MOURNING_FOREST,
"K2": GIANTS_PLAYGROUND,
"K3": GIANTS_PLAYGROUND,
"K4": GIANTS_PLAYGROUND,
"K5": GIANTS_PLAYGROUND,
"K6": GIANTS_PLAYGROUND,
"K7": GIANTS_PLAYGROUND,
"K8": GIANTS_PLAYGROUND,
"K9": GIANTS_PLAYGROUND,
"K10": SCARS,
"K11": SCARS,
"L0": BLIGHTLANDS,
"L1": BLIGHTLANDS,
"L2": BLIGHTLANDS,
"L3": BLIGHTLANDS,
"L4": GIANTS_PLAYGROUND,
"L5": GIANTS_PLAYGROUND,
"L6": GIANTS_PLAYGROUND,
"L7": GIANTS_PLAYGROUND,
"L8": GIANTS_PLAYGROUND,
"L9": SCARS,
"L10": SCARS,
"L11": SCARS,
"M0": BLIGHTLANDS,
"M1": BLIGHTLANDS,
"M2": BLIGHTLANDS,
"M3": BLIGHTLANDS,
"M4": SENTINEL_WOODS,
"M5": SENTINEL_WOODS,
"M6": SENTINEL_WOODS,
"M7": SENTINEL_WOODS,
"M8": SCARS,
"M9": SCARS,
"M10": SCARS,
"M11": SCARS,
"N0": BLIGHTLANDS,
"N1": BLIGHTLANDS,
"N2": BLIGHTLANDS,
"N3": BLIGHTLANDS,
"N4": SENTINEL_WOODS,
"N5": SENTINEL_WOODS,
"N6": SENTINEL_WOODS,
"N7": SENTINEL_WOODS,
"N8": SENTINEL_WOODS,
"N9": SCARS,
"N10": SCARS,
"N11": SCARS
}

ELEMENTS = [
    "fire",
    "smoke",
    "wind",
    "water",
    "plant",
    "frost"
]

BEASTS = [
    "Giant Fly",
    "Rat",
    "Littlefoot",
    "Featherclaw",
    "Wild Boar",
    "Blackbear",
    "Wolf",
    "Mouintain Lion",
    "Giant Leech",
    "Shark",
    "Brown Bear",
    "Giant Spider",
    "Moose",
    "Dire wolf",
    "Saber-toothed Tiger",
    "Giant Elk",
    "Sharp Tooth",
    "Three Horn",
    "Elephant",
    "Huge Polar Bear",
    "Giant Crab",
    "Snarlbeak"
]

def get_hex_region(hex_name):
    if hex_name in HEX_REGION_MAP:
        return HEX_REGION_MAP[hex_name]
    return MAJOR_ROADS

def roll_road_encounter():
    return get_roads_encounter()

def roll_region_encounter(hex_obj):
    hx = hex_obj["name"]
    if hx in HEX_REGION_MAP:
        region = HEX_REGION_MAP[hx]
        output = ""
        if region == UNBROKEN_MOUNTAIN:
            return get_mountain_encounter(hex_obj)
        elif region == GIANTS_PLAYGROUND:
            return get_playground_encounter(hex_obj)
        elif region == MOURNING_FOREST:
            return get_mourning_encounter(hex_obj)
        elif region == BLIGHTLANDS:
            return get_blightlands_encounter(hex_obj)
        elif region == SENTINEL_WOODS:
            return get_sentinel_encounter(hex_obj)
        elif region == SCARS:
            return get_scars_encounter(hex_obj)
        elif region == NORTH_OMARIA:
            return get_omaria_encounter(hex_obj)
        elif region == WATER:
            return get_water_encounter(hex_obj)
    raise Exception("Hex " + hx + " does not exist.")


def get_mountain_encounter(hex_obj):
    if d(6) != 1:
        return "No Encounter"
    monster = random.choice(["White Dragon", "Red Dragon", "Black Dragon", "Gold Dragon", "Giant Polar bear", "miners"])
    motive = random.choice(["seeking morality", "melting snow", "smoking", "searching for gold", "hibernate", "prospecting"])
    complication = random.choice(["lonely", "climate", "no tobacco", "got lost", "hungry", "disease"])
    encounter = f"**Creature:** {monster}, **Motive:** {motive}, **Complication:** {complication}"
    perception_dc = random.randint(1, 10) + random.randint(1, 10) + 2
    stealth_dc = random.randint(1, 10) + random.randint(1, 10) + 2
    perception = f"DC{perception_dc} WIS check to spot at 300ft instead of 100ft."
    stealth = f"DC{stealth_dc} DEX check to avoid detection."
    return f"{encounter}\n{perception}\n{stealth}"


def get_playground_encounter(hex_obj):    
    if d(6) != 1:
        return "No Encounter"
    giant_count = random.randint(2, 5)
    monster = random.choice([f"{giant_count} dwarf giants", "Field Giant", "Red Giant", "Blue Giant", "Green Giant", "Giant Elk"])
    motive = random.choice(["Wrestling", "Drawing in dirt", "patrolling", "watering flowers", "Waiting", "Grazing"])
    complication = random.choice(["Giant ants", "Bad breath", "Broken tools", "no water", "impatient", "allergies"])

    """
    Uncomment once giants are slain
    hunters = random.randint(1, 4) + random.randint(1, 4) + random.randint(1, 4)
    bandits = random.randint(1, 4) + random.randint(1, 4) + random.randint(1, 4)
    monster = random.choice(["Alchemist", f"Band of {bandits} bandits", f"{f} Bow Hunters", "Three horn", "Sharp Tooth", "Giant Elk"])
    motive = random.choice(["finding ingredients", "robbing", "stalking prey", "wrestling", "Hunting", "Grazing"])
    complication = random.choice(["lost", "starving", "ate moon grass", "drunken", "parasites", "Injured foot"])
    """
    encounter = f"**Encounter:**\n **Creature:** {monster}, **Motive:** {motive}, **Complication:** {complication}"
    perception_dc = random.randint(1, 10) + random.randint(1, 10) + 2
    stealth_dc = random.randint(1, 10) + random.randint(1, 10) + 2
    perception = f"DC{perception_dc} WIS check to spot at 300ft instead of 100ft."
    stealth = f"DC{stealth_dc} DEX check to avoid detection."
    return f"{encounter}\n{perception}\n{stealth}"

def get_mourning_encounter(hex_obj):
    if d(6) != 1:
        return "No Encounter"
    d4 = random.randint(1, 4)
    twod4 = d4 + random.randint(1, 4)
    threed4 = twod4 + random.randint(1, 4)
    encounter = random.choice([
        f"{d4} Shadows",
        "Specter of " + random.choice(['primordial', "titan soldier", "dragon slayer"]),
        f"{twod4} skeletons op " + random.choice(['primordials', "titan soldiers", "dragon slayers"]),
        f"{d4} Dire Wolves",
        f"Saber-toothed tiger",
        "Sharp Tooth",
        "Three horn",
        f"{threed4} Littlefoots",
        f"{twod4} Featherclaws",
        "bone heap displaying as mass grave in pit"
    ])
    encounter = "**Encounter:** " + encounter
    perception_dc = random.randint(1, 10) + random.randint(1, 10) + random.randint(1, 10) + 2
    stealth_dc = random.randint(1, 8) + random.randint(1, 8) + 2
    perception = f"DC{perception_dc} WIS check to spot at 100ft instead of 30ft."
    stealth = f"DC{stealth_dc} DEX check to avoid detection."
    return f"{encounter}\n{perception}\n{stealth}"

def get_blightlands_encounter(hex_obj):
    if d(3) != 1:
        return "No Encounter"
    d4 = random.randint(1, 4)
    twod6 = random.randint(1, 6) + random.randint(1, 6)
    encounter = random.choice([
        "Root Walker",
        "Grass Heap",
        f"{d4} Shroom People",
        f"{twod6} slimy skeletons",
        "Werewolf",
        "Black Slime",
        "Pink Slime",
        "Green Giant",
        f"{d4} Chaos shells",
        f"{twod6} leech men"
    ])
    encounter = "**Encounter:** " + encounter
    
    perception_dc = random.randint(1, 10) + random.randint(1, 10) + random.randint(1, 10) + 2
    stealth_dc = random.randint(1, 8) + random.randint(1, 8) + 2
    perception = f"DC{perception_dc} WIS check to spot at 100ft instead of 30ft."
    stealth = f"DC{stealth_dc} DEX check to avoid detection."
    return f"{encounter}\n{perception}\n{stealth}"

def choice(list):
    return random.choice(list)

def d(size):
    return random.randint(1, size)

def get_sentinel_encounter(hex_obj):
    if d(3) != 1:
        return "No Encounter"
    encounter = random.choice([
        choice(ELEMENT) + " elemental " + choice(BEASTS),
        "Fey guardian of " + choice(ELEMENT),
        "Diminutive Nymph of " + choice(ELEMENT),
        choice(ELEMENT) + " nymph",
        "Major Nymph of "+ choice(ELEMENT),
        "Arch Fey of " + choice(ELEMENT),
    ])
    encounter = "**Encounter:** " + encounter
    
    perception_dc = random.randint(1, 10) + random.randint(1, 10) + random.randint(1, 10) + 2
    stealth_dc = random.randint(1, 8) + random.randint(1, 8) + 2
    perception = f"DC{perception_dc} WIS check to spot at 100ft instead of 30ft."
    stealth = f"DC{stealth_dc} DEX check to avoid detection."
    return f"{encounter}\n{perception}\n{stealth}"

def get_scars_encounter(hex_obj):
    # 2d6 table
    d4 = random.randint(1, 4)
    roll = random.randint(1, 6) + random.randint(1, 6)
    encounter = ""
    roll_map = {
        2: "Great sand worm Volheis",
        3: "Sand pirates piloting three-story hovering wind ship",
        4: f"{d4} sand guardians",
        5: f"Pit Fisher",
        6: "Only the blowing sands accompany you on your journey.",
        7: "Only the blowing sands accompany you on your journey.",
        8: "Only the blowing sands accompany you on your journey.",
        9: "Lost wanderer " + random.choice(["child", "trader", "tiger cultist", "sentinel", "silent"]),
        10: "Wandering oasis. Water source.",
        11: "Group of dying travelers: " + random.choice(["omarian scouts", "dwarf giants", "smugglers", "rebels", "traders"]),
        12: "King Yevor's Wandering Temple" 
    }
    encounter = roll_map[roll]
        
    encounter = "**Encounter:** " + encounter
    perception_dc = random.randint(1, 10) + random.randint(1, 10) + 2
    stealth_dc = random.randint(1, 10) + random.randint(1, 10) + random.randint(1, 10) + 2
    perception = f"DC{perception_dc} WIS check to spot at 300ft instead of 100ft."
    stealth = f"DC{stealth_dc} DEX check to avoid detection."
    return f"{encounter}\n{perception}\n{stealth}"

def get_omaria_encounter(hex_obj):
    if d(3) != 1:
        return "No Encounter"
    creature = random.choice(["hunting party", "shaman", "major nymph", "Flesh Eater", "giant ant(red)", "thief", "brown bear"])
    motive = random.choice(["hunting", "rescuing animals", "mischief", "convert people", "recruit helper", "rob others", "hunt food"])
    complication = random.choice(["broken gear", "stuck", "lonely", "hunger", "distracted by partner", "got robbed", "thorn in foot"])
    encounter = f"**Encounter:** Creature: {creature}, Motive: {motive}, Complication: {complication}"
    perception_dc = random.randint(1, 10) + random.randint(1, 10) + 2
    stealth_dc = random.randint(1, 10) + random.randint(1, 10) + random.randint(1, 10) + 2
    perception = f"DC{perception_dc} WIS check to spot at 300ft instead of 100ft."
    stealth = f"DC{stealth_dc} DEX check to avoid detection."
    return f"{encounter}\n{perception}\n{stealth}"

def get_roads_encounter():
    if d(3) != 1:
        return "No Encounter"
    species = ["pink human with red eyes", "pointy-eared green human", "pale grey human", "blue human with black hair", "human", "foxfolk", "lynxfolk", "rabbitfolk", "raccoonfolk", "ratfolk"]
    encounter = random.choice([
        "Wayfarers: " + random.choice(["Dragon Troupe", "Factfinders", "Blackstrap's Mercenaries", "The Silent Caravan", "Othercook's Adventuring Company", "Wraith Recon", "Printers, Inc", "Disciples of Bimros"]),
        "Omarian militia " + random.choice([
            "manning a checkpoint",
            "patrolling",
            "collecting taxes",
            "looking for a fugitive " + random.choice(["murderer","unlicensed magic user", "thief", "rebel"]),
            "fighting a " + random.choice(["pincer beast", "giant crab", "giant elk"]),
            "on leave and looking for excitement",
            "en route to contract",
            "escorting prisoners, " + random.choice(["rebels", "thieves", "assassins", "magic users"]),
            "escorting " + random.choice(["bronzehammers", "goldrobe nobles", "goldrobe royals", "coggers"]),
            "transporting " + random.choice(["200gp worth of golrobe possessions", "crates of 100 light crossbows", "grain tribute", "horse tribute"]),
            "carrying their wounded after a recent fight with rebels"
        ]),
        "Omarian scouts " + random.choice([
            "hauling a captured dwarf giant",
            "performing training exercises with " + random.choice([
                "mobility gear",
                "horseback archery",
                "archery on foot",
                "stealth maneuvers",
                "sword fighting"
            ]),
            "celebrating kiling a giant by drinking heavily",
            "digging graves after having fought and killed a giant"
        ]),
        "Group of traveling " + random.choice(["goldrobes", "silent", "coggers", "bronzehammers", "soots"]),
        "A lone child who " + random.choice([
            "were separated from parents headed to destination",
            "are an orphan traveling for new life",
            "were abandoned on the road",
            "parents were killed by giants",
            "is an Omarian royal who escaped kidnapping",
            "is used as bait for a group of bandits"
        ]),
        "a dog who " + random.choice([
            "carries a bronze family hammer in its mouth",
            "has three legs",
            "can talk(cursed human)",
            "looks part wolf",
            "tries to lead the party to save it's owners from " + random.choice(["passing out on road", "having fallen into a well", "a brown bear that chased owners up a tree"])
        ]),
        "a bear caught in a beartrap" + random.choice(["", "", "(secretly shaman)"]),
        "beggar asking for food, water, and gold" + random.choice(["", "", "(secretly celestial)"]),
        'a group of highwaymen in shabby Omarian uniforms who collect a "toll" of 10gp'
    ])
    encounter = "**Encounter:** " + encounter
    perception_dc = random.randint(1, 10) + random.randint(1, 10) + 2
    stealth_dc = random.randint(1, 10) + random.randint(1, 10) + random.randint(1, 10) + 2
    perception = f"DC{perception_dc} WIS check to spot at 300ft instead of 100ft."
    stealth = f"DC{stealth_dc} DEX check to avoid detection."
    return f"{encounter}\n{perception}\n{stealth}"

def get_water_encounter(hex_obj):
    encounter = random.choice([
        "Reacher(from monstrosity.txt)",
        "3 sharks",
        "ship of 30 privateers",
        "Giant crab",
        "flock of 10 Snarlbeaks",
        "wirlpool",
        "abandoned merchant ship full of skeletons",
        "ghost of the invincible"
    ])
    encounter = "**Encounter:** " + encounter
    perception_dc = random.randint(1, 10) + random.randint(1, 10) + 2
    stealth_dc = random.randint(1, 10) + random.randint(1, 10) + random.randint(1, 10) + 2
    perception = f"DC{perception_dc} WIS check to spot at 500ft instead of 100ft."
    return f"{encounter}\n{perception}"
