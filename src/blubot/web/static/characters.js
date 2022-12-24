const ERROR = "error";

// Misc Stats
const NAME = "name"
const XP = "xp"; // Experience Points
const AC = "ac"; // Armor Class
const HP = "hp"; // Hit Points
const THP = "thp"; // Temporary Hit Points
const CLASS = "class";
const SIZE = "size";
const CULTURE = "culture";
const SPEED = "speed";
const BODY_TYPE = "body type";
const STAMINA_DICE = "stamina dice";
const ARMOR_PROF = "armor proficiencies";
const WEAPON_PROF = "weapon proficiencies";
const TOOL_PROF = "tool proficiencies";
const LANGUAGES = "languages";
const PROF_BONUS = "prof bonus";
const VISION = "vision";
const CONDITIONS = "conditions";
const UNUSED = "unused";

// Abilities
const ABILITIES = "abilities";
const STRENGTH = "strength";
const DEXTERITY = "dexterity";
const CONSTITUTION = "constitution";
const INTELLIGENCE = "intelligence";
const WISDOM = "wisdom";
const CHARISMA = "charisma";
const ABILITIES_LIST = [STRENGTH, DEXTERITY, CONSTITUTION, INTELLIGENCE, WISDOM, CHARISMA];
const SAVING_THROWS = "saving throws";

// Skills
const SKILLS = "skills";
const ATHLETICS = "athletics";
const ACROBATICS = "acrobatics";
const SLEIGHT_OF_HAND = "sleight of hand";
const STEALTH = "stealth";
const ARCANA = "arcana";
const HISTORY = "history";
const INVESTIGATION = "investigation";
const NATURE = "nature";
const RELIGION = "religion";
const ANIMAL_HANDLING = "animal handling";
const INSIGHT = "insight";
const MEDICINE = "medicine";
const PERCEPTION = "perception";
const SURVIVAL = "survival";
const DECEPTION = "deception";
const INTIMIDATION = "intimidation";
const PERFORMANCE = "performance";
const PERSUASION = "persuasion";
const SKILLS_LIST = [ATHLETICS, ACROBATICS, SLEIGHT_OF_HAND, STEALTH, ARCANA, HISTORY, INVESTIGATION, NATURE, RELIGION, ANIMAL_HANDLING, INSIGHT, MEDICINE, PERCEPTION, SURVIVAL, DECEPTION, INTIMIDATION, PERFORMANCE, PERSUASION]
const SKILL_ABILITY_MAP = {
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
};

// Inventory
const INVENTORY = "inventory";

// Attacks
const ATTACKS = "attacks";
const ATTACK_NAME = "attack name";
const TO_HIT = "to hit";
const DAMAGE = "damage";
const DAMAGE_TYPE = "damage type";

$(document).ready(function(){
    $("#text_json").val(""); // Clear this out. Seems to want to keep values when refreshing
    $("#button_copy").click(function(){
        var text_json = $("#text_json").val();
        navigator.clipboard.writeText(text_json);
    });


});