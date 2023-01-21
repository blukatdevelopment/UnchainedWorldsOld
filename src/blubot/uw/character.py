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
BODY_TYPE = "body type"
STAMINA_DICE = "stamina dice"
ARMOR_PROF = "armor proficiencies"
WEAPON_PROF = "weapon proficiencies"
TOOL_PROF = "tool proficiencies"
LANGUAGES = "languages"
PROF_BONUS = "prof bonus"
VISION = "vision"
CONDITIONS = "conditions"
UNUSED = "unused"

# Abilities
ABILITIES = "abilities"
STRENGTH = "strength"
DEXTERITY = "dexterity"
CONSTITUTION = "constitution"
INTELLIGENCE = "intelligence"
WISDOM = "wisdom"
CHARISMA = "charisma"
ABILITIES_LIST = [STRENGTH, DEXTERITY, CONSTITUTION, INTELLIGENCE, WISDOM, CHARISMA]
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

NECESSARY_FIELDS = [NAME, XP, HP, AC, CLASS, SIZE, CULTURE, SPEED, BODY_TYPE, STAMINA_DICE, ARMOR_PROF, WEAPON_PROF, TOOL_PROF, LANGUAGES, PROF_BONUS, ABILITIES, SKILLS, INVENTORY, ATTACKS, SAVING_THROWS]

def parse_character(raw_json):
    errors = []
    try:
        character_dict = json.loads(raw_json)
    except:
        return {ERROR: "malformed json"}
    sanitized = {}
    for field in NECESSARY_FIELDS:
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
    if raw_json is None:
        return None
    return parse_character(raw_json)

def load_active_status(db, user_id, character):
    raw_json = db.get_active_character_status(user_id)
    if raw_json is None or raw_json == "":
        return init_status(character)
    return json.loads(raw_json)

def init_status(character):
    status = {
        HP: character[HP],
        THP: 0,
        STAMINA_DICE: character[STAMINA_DICE]
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
    if attack is None:
        return f'No such attack: {attack_name}. Meow.'
    to_hit = attack[TO_HIT]
    damage = attack[DAMAGE]
    damage_type = attack[DAMAGE_TYPE]
    
    (msg) = roll_attack(attack_name, to_hit, damage, damage_type)
    return msg

def is_valid_check_type(check_type):
    return check_type.lower() in SKILLS_LIST or check_type.lower() in ABILITIES_LIST 

def is_valid_ability(ability):
    return ability.lower() in ABILITIES_LIST

def get_check_modifier(check_type, character):
    if check_type.lower() in ABILITIES_LIST:
        score = get_ability_score(check_type.lower(), character)
        return get_ability_modifier(score)
    elif check_type.lower() in SKILLS_LIST:
        score = get_ability_score(SKILL_ABILITY_MAP[check_type.lower()], character)
        mod = get_ability_modifier(score)
        if check_type.lower() in character[SKILLS]:
            return mod + character[PROF_BONUS]
        return mod
    else:
        print(f"Invalid check type: {check_type}")
        return 0

def get_save_modifier(ability, character):
    mod = 0
    if ability.lower() in ABILITIES_LIST:
        score = get_ability_score(ability.lower(), character)
        mod += get_ability_modifier(score)
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
    print(f"Invalid ability: {ability}")
    return -1

def get_ability_modifier(ability_score):
    if ability_score < 3:
        return -4
    if ability_score < 5:
        return -3
    if ability_score < 7:
        return -2
    if ability_score < 9:
        return -1
    if ability_score < 11:
        return 0
    if ability_score < 13:
        return 1
    if ability_score < 15:
        return 2
    if ability_score < 17:
        return 3
    if ability_score < 19:
        return 4
    if ability_score < 21:
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
    if character is None:
        return f"No Active character selected."
    status = load_active_status(bot.db, ctx.user.id, character)
    if change < 0:
        status['thp'] += change
        if status['thp'] < 0:
            status['hp'] += status['thp']
            status['thp'] = 0
    else:
        status['hp'] += change

    save_status(bot.db, ctx.user.id, status)
    msg = f"{character['name']}'s HP "
    msg += 'drops' if change < 0 else 'increases'
    msg += f' by {change}\n'
    msg += format_status(status, character)
    return msg

def format_status(status, character):
        msg = f"HP: {status['hp']}/{character['hp']}"
        if status["thp"] > 0:
            msg += f"({status['thp']})\n"
        else:
            msg += "\n"
        msg += f"Stamina Dice: {status['stamina dice']}/{character['stamina dice']}"
        return msg