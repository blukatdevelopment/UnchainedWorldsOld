
# This Script should create a random character for Unchained worlds: Basic Edition
# This follows the four step process of name, ability scores, gear, and appearance
import random
from person_gen import get_common_name

def get_name():
    return get_common_name()

def roll_2d6():
    return random.randint(1, 6) + random.randint(1, 6)

def roll_3d6():
    return random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)

def get_abilities():
    abilities = []
    # 3d6 down the line
    for i in range(6):
        abilities.append(roll_3d6())
    random_score = random.randint(0, 5)

    # try to Replace a random score with 14
    if abilities[random_score] < 14:
        abilities[random_score] = 14
    # or, just any of them, I guess
    else:
        for i in range(6):
            score = abilities[i]
            if score < 14:
                abilities[i] = 14
                break

    return abilities

def get_gear():
    gear = []
    gear.append("Common clothes")
    item = random.choice([
        "4 Torches",
        "Waterskin",
        "Pitchfork",
        "Bow and 5 arrows",
        "Rope (50ft)",
        "4 Dry Rations"])
    if item == "Bow and 5 arrows":
        gear.append("Bow")
        gear.append("5 arrows")
    else:
        gear.append(item)
    return gear

def get_appearance():
    if random.randint(1, 2) == 1:
        return get_bimran_appearance()
    else:
        return get_beastfolk_appearance()

def get_bimran_appearance():
    return "Bimran"

def get_beastfolk_appearance():
    return "Beastfolk"

def get_character():
    character = {}
    character["name"] = get_name()
    character["abilities"] = get_abilities()
    character["gear"] = get_gear()
    character["appearance"] = get_appearance()
    return character

def generate_ten_characters():
    for i in range(10):
        print(get_character())

def main():
    generate_ten_characters()

main()