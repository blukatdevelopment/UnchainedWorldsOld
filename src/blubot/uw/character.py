import json
from uw.dice import roll_attack

ERROR = "error"

# Misc Stats
NAME = "name"
XP = "xp" # Experience Points
AC = "ac" # Armor Class
HP = "hp" # Hit Points
THP = "thp" # Temporary Hit Points
CLASS = "class"
SIZE = "size"
CULTURE = "culture"
SPEED = "speed"
STAMINA_DICE = "stamina dice"
ARMOR_PROF = "armor proficiencies"
WEAPON_PROF = "weapon proficiencies"
TOOL_PROF = "tool proficiencies"
LANGUAGES = "languages"
PROF_BONUS = "prof bonus"
VISION = "vision"
CONDITIONS = "conditions"
UNUSED = "unused"
IMAGE = "image"
FEATS = "feats"

# Abilities
ABILITIES = "abilities"
STRENGTH = "strength"
DEXTERITY = "dexterity"
CONSTITUTION = "constitution"
INTELLIGENCE = "intelligence"
WISDOM = "wisdom"
CHARISMA = "charisma"
ABILITIES_LIST = [STRENGTH, DEXTERITY, CONSTITUTION, INTELLIGENCE, WISDOM, CHARISMA]
ABILITIES_LIST_ABBREVIATED = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
ABILITIES_ABBREVIATED_MAP = {
    "STR": STRENGTH,
    "DEX": DEXTERITY, 
    "CON": CONSTITUTION, 
    "INT": INTELLIGENCE, 
    "WIS": WISDOM, 
    "CHA": CHARISMA
}
SAVING_THROWS = "saving throws"

# Skills
SKILLS = "skills"
ATHLETICS = "athletics"
ACROBATICS = "acrobatics"
SLEIGHT_OF_HAND = "sleight of hand"
STEALTH = "stealth"
ARCANA = "arcana"
HISTORY = "history"
INVESTIGATION = "investigation"
NATURE = "nature"
RELIGION = "religion"
ANIMAL_HANDLING = "animal handling"
INSIGHT = "insight"
MEDICINE = "medicine"
PERCEPTION = "perception"
SURVIVAL = "survival"
DECEPTION = "deception"
INTIMIDATION = "intimidation"
PERFORMANCE = "performance"
PERSUASION = "persuasion"
SKILLS_LIST = [ATHLETICS, ACROBATICS, SLEIGHT_OF_HAND, STEALTH, ARCANA, HISTORY, INVESTIGATION, NATURE, RELIGION, ANIMAL_HANDLING, INSIGHT, MEDICINE, PERCEPTION, SURVIVAL, DECEPTION, INTIMIDATION, PERFORMANCE, PERSUASION]
SKILL_ABILITY_MAP = {
    ATHLETICS: STRENGTH,
    ACROBATICS: DEXTERITY,
    SLEIGHT_OF_HAND: DEXTERITY,
    STEALTH: DEXTERITY,
    ARCANA: INTELLIGENCE,
    HISTORY: INTELLIGENCE,
    INVESTIGATION: INTELLIGENCE,
    NATURE: INTELLIGENCE,
    RELIGION: INTELLIGENCE,
    ANIMAL_HANDLING: WISDOM,
    INSIGHT: WISDOM,
    MEDICINE: WISDOM,
    PERCEPTION: WISDOM,
    SURVIVAL: WISDOM,
    DECEPTION: CHARISMA,
    INTIMIDATION: CHARISMA,
    PERFORMANCE: CHARISMA,
    PERSUASION: CHARISMA
}

# Inventory
INVENTORY = "inventory"

# Attacks
ATTACKS = "attacks"
ATTACK_NAME = "attack name"
TO_HIT = "to hit"
DAMAGE = "damage"
DAMAGE_TYPE = "damage type"

REQUIRED_FIELDS = [NAME, XP, HP, AC, CLASS, SIZE, CULTURE, SPEED, STAMINA_DICE, ARMOR_PROF, WEAPON_PROF, TOOL_PROF, LANGUAGES, PROF_BONUS, ABILITIES, SKILLS, INVENTORY, ATTACKS, SAVING_THROWS, FEATS]

def parse_character(raw_json):
    errors = []
    try:
        character_dict = json.loads(raw_json)
    except:
        return {ERROR: "malformed json"}
    sanitized = {}
    for field in REQUIRED_FIELDS:
        if field not in character_dict:
            errors.append(f"missing field {field}")
        else:
            sanitized[field] = character_dict[field]
    if len(errors) > 0:
        return {ERROR: "\n".join(errors)}
    if not abilities_valid(character_dict[ABILITIES]):
        return {ERROR: "Abilities are invalid. You need six, and they need to be between 1 and 20."}


    return sanitized

def load_active_character(db, user_id):
    raw_json = db.get_active_character(user_id)
    if raw_json == None:
        return None
    return parse_character(raw_json)

def load_active_status(db, user_id, character):
    raw_json = db.get_active_character_status(user_id)
    if raw_json == None or raw_json == "":
        return init_status(character)
    status = json.loads(raw_json)
    status[HP] = coerce_to_int(status[HP])
    status[THP] = coerce_to_int(status[THP])
    status[STAMINA_DICE] = coerce_to_int(status[STAMINA_DICE])
    return status

def coerce_to_int(field):
    if field == '' or field == None:
        return 0
    if isinstance(field, int):
        return field
    if field.isdigit():
        return int(field)
    return 0

def init_status(character):


    status = {
        HP: coerce_to_int(character[HP]),
        THP: 0,
        STAMINA_DICE: coerce_to_int(character[STAMINA_DICE])
    }
    return status

def save_status(db, user_id, status):
    raw_json = json.dumps(status)
    db.update_active_character_status(user_id, raw_json)

def abilities_valid(abilities):
    if len(abilities) != 6:
        return False
    for ability in abilities:
        if ability < 0 or ability > 20:
            return False
    return True

def list_attacks(character):
    attacks = []
    for attack in character[ATTACKS]:
        attacks.append(attack[ATTACK_NAME])
    msg = f'Attacks for {character[NAME]}: '
    msg += ', '.join(attacks)
    msg += "."
    return msg

def use_attack(character, attack_name):
    attack_name = attack_name.lower()
    attack = None
    for current_attack in character[ATTACKS]:
        if current_attack[ATTACK_NAME].lower() == attack_name:
            attack = current_attack
    
    if attack == None:
        return f"No such attack: {attack_name}. Meow."
    to_hit = int(attack[TO_HIT])
    damage = attack[DAMAGE]
    damage_type = attack[DAMAGE_TYPE]

    msg = roll_attack(attack_name, to_hit, damage, damage_type)[0]
    return f"{character['name']} uses their {attack_name} attack!\n" + msg

def parse_ability(ability):
    if ability.lower() in ABILITIES_LIST:
        return ability.lower()
    if ability.upper() in ABILITIES_LIST_ABBREVIATED:
        return ABILITIES_ABBREVIATED_MAP[ability.upper()]
    return ""

def get_ability_modifier(check_type, character):
    if check_type.lower() in ABILITIES_LIST:
        score = get_ability_score(check_type.lower(), character)
        return get_ability_modifier_from_score(score)
    return 0

def get_skill_info(character):
    skill_info = {
        PROF_BONUS: character[PROF_BONUS],
        WEAPON_PROF: character[WEAPON_PROF],
        ARMOR_PROF: character[ARMOR_PROF],
        TOOL_PROF: character[TOOL_PROF],
        LANGUAGES: character[LANGUAGES],
        SKILLS: character[SKILLS]
    }
    return skill_info

def get_save_modifier(ability, character):
    mod = 0
    if ability.lower() in ABILITIES_LIST:
        score = get_ability_score(ability.lower(), character)
        mod += get_ability_modifier_from_score(score)
    for save in character[SAVING_THROWS]:
        if save == ability.lower():
            mod += character[PROF_BONUS]
    return mod

def get_ability_score(ability, character):
    if ability == STRENGTH:
        return character[ABILITIES][0]
    if ability == DEXTERITY:
        return character[ABILITIES][1]
    if ability == CONSTITUTION:
        return character[ABILITIES][2]
    if ability == INTELLIGENCE:
        return character[ABILITIES][3]
    if ability == WISDOM:
        return character[ABILITIES][4]
    if ability == CHARISMA:
        return character[ABILITIES][5]
    return -1

def get_ability_modifier_from_score(ability_score):
    if ability_score <= 3:
        return -4
    if ability_score <= 5:
        return -3
    if ability_score <= 7:
        return -2
    if ability_score <= 9:
        return -1
    if ability_score <= 11:
        return 0
    if ability_score <= 13:
        return 1
    if ability_score <= 15:
        return 2
    if ability_score <= 17:
        return 3
    if ability_score <= 19:
        return 4
    if ability_score <= 20:
        return 5

def xp_to_level(xp):
    if xp < 300:
        return 1
    elif xp < 900:
        return 2
    elif xp < 1800:
        return 3
    elif xp < 3600:
        return 4
    elif xp < 6100:
        return 5
    elif xp < 9100:
        return 6
    elif xp < 13100:
        return 7
    elif xp < 22600:
        return 8
    elif xp < 44600:
        return 9
    else:
        return 10

def update_hp(ctx, bot, change):
    character = load_active_character(bot.db, ctx.user.id)
    if character == None:
        return f"No Active character selected."
    status = load_active_status(bot.db, ctx.user.id, character)
    if change < 0:
        status[THP] += change
        if status[THP] < 0:
            status[HP] += status[THP]
            status[THP] = 0
    else:
        status[HP] += change

    save_status(bot.db, ctx.user.id, status)
    msg = f"{character['name']}'s HP "
    msg += 'drops' if change < 0 else 'increases'
    msg += f' by {change}\n'
    msg += format_status(status, character)
    return msg

def format_status(status, character):
        msg = f"HP: {status[HP]}/{character[HP]}"
        if status[THP] > 0:
            msg += f"({coerce_to_int(status[THP])})\n"
        else:
            msg += "\n"
        msg += f"Stamina Dice: {status[STAMINA_DICE]}/{coerce_to_int(character[STAMINA_DICE])}"
        return msg