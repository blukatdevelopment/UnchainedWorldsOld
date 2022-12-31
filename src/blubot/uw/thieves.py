import random

TARGET_OBJECT = [
"Gem",
"Jewelry",
"Statue",
"clothing",
"furniture",
"key",
"document",
"information",
"Magic Item",
"Diamond",
"Scroll",
"animal",
"food",
"monster part",
"alchemy ingredient",
"lost tech item",
"mystery container",
"gold"
]

COMPLICATIONS = [
"Competing thieves",
"Extra guards",
"Assassin",
"Mercenaries",
"Monsters",
"Relocated",
"Must be captured in transit",
"Locate, but do not steal",
"Already stolen",
"Ambush. False target."
]


COPPER_RING = "Copper ring"
SILVER_RING = "Silver ring"
GOLD_CORE = "Gold core"
THIERSGAR = "Thiersgar"
GIANTS_PLAYGROUND = "Giant's playground"

TARGET_LOCATION = [
    COPPER_RING,
    SILVER_RING,
    GOLD_CORE,
    THIERSGAR,
    GIANTS_PLAYGROUND
]

FLAVOR_WORDS = [
"Stinky",
"Warm",
"Cold",
"Gross",
"Stylish",
"Ancient",
"Imported",
"Gaudy",
"Rancid",
"Perfumed",
"Golden",
"Invisible",
"Fire",
"Iron",
"Silver",
"Steel",
"Jade",
"Red",
"Yellow",
"Green",
"Blue",
"Purple",
"Indego",
"Crimson",
"Illegal",
"Sacriligeous",
"Forbidden",
"Beloved",
"Feline",
"Canine",
"Holy",
"Unholy",
"Popular",
"Famous",
"Infamous",
"Marriage",
"Courageous",
"Equine",
"Avian",
"Crunchy",
"Smooth",
"Transparent",
"Opaque",
"Glossy",
"Silent",
"Soot",
"Cogger",
"Bronzehammer",
"Goldrobe",
"Field Folk",
"Wildfolk",
"Holiday",
"Festive",
"Grave",
"Memorial"
]

def location_reward(location):
    if location == COPPER_RING:
        rewards = ["10gp", "15gp", "20gp", "25gp"]
        return random.choice(rewards)
    if location == THIERSGAR:   
        rewards = ["20gp", "30gp", "50gp", "75gp"]
    if location == SILVER_RING:
        rewards = ["25gp", "50gp", "75gp", "100gp"]
        return random.choice(rewards)
    if location == GIANTS_PLAYGROUND:
        rewards = ["100gp", "150gp", "200gp", "250gp"]
        return random.choice(rewards)
    if location == GOLD_CORE:
        rewards = ["250gp", "500gp", "750gp", "1000gp"]
        return random.choice(rewards)
        return random.choice(rewards)

def flavor_words():
    return f"{random.choice(FLAVOR_WORDS)}, {random.choice(FLAVOR_WORDS)}, {random.choice(FLAVOR_WORDS)}"

def thieves_prompt():
    location = random.choice(TARGET_LOCATION)
    reward = location_reward(location) 
    msg = '```json\n{\n'
    msg += f'\t"Target": "{random.choice(TARGET_OBJECT)}",\n'
    msg += f'\t"Location": "{location}",\n'
    msg += f'\t"Reward": "{reward}",\n'
    msg += f'\t"Flavor words": "{flavor_words()}"\n'
    msg += '}```'
    return msg