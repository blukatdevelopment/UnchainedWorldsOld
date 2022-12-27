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
const SENSES = "senses";
const IMG = "image";
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



// Abilities helpers
function get_ability_mod_id(ability){
    switch(ability) {
        case STRENGTH:
            return "STR_MOD";
            break;
        case DEXTERITY:
            return "DEX_MOD";
            break;
        case CONSTITUTION:
            return "CON_MOD";
            break;
        case INTELLIGENCE:
            return "INT_MOD";
            break;
        case WISDOM:
            return "WIS_MOD";
            break;
        case CHARISMA:
            return "CHA_MOD";
            break;
    }
}

function set_ability_mod(ability, mod){
    var id = get_ability_mod_id(ability);
    var mod_text = "";
    if(mod > -1){
        mod_text += "+";
    }
    mod_text += mod;
    $("#"+id).text(mod_text);
}

function get_ability_score_id(ability){
    switch(ability) {
        case STRENGTH:
            return "STR_SCORE_TXT";
            break;
        case DEXTERITY:
            return "DEX_SCORE_TXT";
            break;
        case CONSTITUTION:
            return "CON_SCORE_TXT";
            break;
        case INTELLIGENCE:
            return "INT_SCORE_TXT";
            break;
        case WISDOM:
            return "WIS_SCORE_TXT";
            break;
        case CHARISMA:
            return "CHA_SCORE_TXT";
            break;
    }
}

function set_ability_score(ability, score){
    var id = get_ability_score_id(ability);
    $("#"+id).val(score);
}

function get_ability_score(ability){
    var id = get_ability_score_id(ability);
    var score = $("#"+id).val();
    return parseInt(score);
}

function calculate_ability_mod(score){
    score = parseInt(score);
    if(score < 2){
        return -5;
    }
    if(score < 4){
        return -4;
    }
    if(score < 6){
        return -3;
    }
    if(score < 8){
        return -2;
    }
    if(score < 10){
        return -1;
    }
    if(score < 12){
        return 0;
    }
    if(score < 14){
        return 1;
    }
    if(score < 16){
        return 2;
    }
    if(score < 18){
        return 3;
    }
    if(score < 20){
        return 4;
    }
    return 5;
}

function update_mods(){
    update_ability_mod(STRENGTH);
    update_ability_mod(DEXTERITY);
    update_ability_mod(CONSTITUTION);
    update_ability_mod(INTELLIGENCE);
    update_ability_mod(WISDOM);
    update_ability_mod(CHARISMA);
}

function update_ability_mod(ability){
    var score = get_ability_score(ability);
    var mod = calculate_ability_mod(score);
    set_ability_mod(ability, mod);
}

function clear_abilities(){
    set_ability_score(STRENGTH, 10);
    set_ability_score(DEXTERITY, 10);
    set_ability_score(CONSTITUTION, 10);
    set_ability_score(INTELLIGENCE, 10);
    set_ability_score(WISDOM, 10);
    set_ability_score(CHARISMA, 10);
    update_mods();
}


// Character sheet JSON generation

function generate_sheet_json(){
    var character = {};
    character = generate_header_fields(character);
    character = generate_abilities(character);
    character = generate_stat_fields(character);
    character = generate_proficiency_fields(character);
    $("#text_json").val(JSON.stringify(character));
}

function generate_abilities(character){
    character[ABILITIES] = [
        get_ability_score(STRENGTH),
        get_ability_score(DEXTERITY),
        get_ability_score(CONSTITUTION),
        get_ability_score(INTELLIGENCE),
        get_ability_score(WISDOM),
        get_ability_score(CHARISMA)
    ];
    return character;
}

function generate_header_fields(character){
    character[NAME] = $("#NAME_TXT").val();
    character[CLASS] = $("#CLASS_TXT").val();
    character[CULTURE] = $("#CULTURE_TXT").val();
    character[BODY_TYPE] = $("#BODY_TXT").val();
    character[XP] = $("#XP_TXT").val();
    return character;
}

function generate_stat_fields(character){
    character[HP] = $("#HP_TXT").val();
    character[AC] = $("#AC_TXT").val();
    character[SIZE] = $("#SIZE_TXT").val();
    character[SPEED] = $("#SPEED_TXT").val();
    character[STAMINA_DICE] = $("#STAMINA_TXT").val();
    character[IMG] = $("#IMG_TXT").val();
    character[SENSES] = $("#SENSES_TXT").val();
    return character;
}

function generate_proficiency_fields(character){
    character[PROF_BONUS] = $("#PROF_TXT").val();
    character[WEAPON_PROF] = $("#WEAPONS_TXT").val();
    character[ARMOR_PROF] = $("#ARMORS_TXT").val();
    character[TOOL_PROF] = $("#TOOLS_TXT").val();

    // Skills
    var skill_list = $("#SKILLS_TXT").val().split(",");
    character[SKILLS] = []
    skill_list.forEach((skill) => {
        var skill_text = skill.trim().toLowerCase();
        character[SKILLS].push(skill_text);
    });

    // Saves
    character[SAVING_THROWS] = [];
    var save_list = $("#SAVES_TXT").val().split(',');
    save_list.forEach((save) => {
        var save_text = save.trim().toLowerCase();
        character[SAVING_THROWS].push(save_text);
    });    
    return character;
}

function clear_feats_table(){
    var header = ["Feats"];
    var row_data = [
        [" "]
    ];
    var table = $("#FEATS_TABLE");
    make_table(table, header, row_data, "feats");
}

/* Table logic
    @table: JQUERY object for table element,
    @header: array of header columns
    @row_data: 2D array containing cell contents

    Creates a table with th of headers columns,
    td for each row, and then buttons to update the
    table afterward.
*/
function make_table(table, header, row_data, blank_row, table_name){
    var btn_row_id = table_name + "_btn";
    table.empty();
    make_header_row(table, header);
    make_table_buttons(table, blank_row, btn_row_id);
    row_data.forEach((row) => {
        add_data_row(table, row, btn_row_id);
    });
    
}

function make_header_row(table, header){
    var header_txt = "<tr>";
    header.forEach((column) => {
        header_txt += "<th>" + column + "</th>";
    });
    header_txt += "</tr>";
    table.append("$" + header_txt);
}

function add_data_row(table, row, btn_row_id){
    var button_row = $("#" + btn_row_id);
    console.log(table.html());
    console.log(button_row.html());
    table.remove(button_row);

    var row_tr = $("<tr>");
    row.forEach(cell_data => {
        var row_td = $("<td>");
        var row_input = $("<input>").attr({ type: 'text'}).val(cell_data);
        row_td.append(row_input);
        row_tr.append(row_td);
    });
    table.append(row_tr);
    table.append(button_row);
}

function make_table_buttons(table, btn_row_id){
    var add_td = $("<td>");
    var add_btn = $("<button>").html("Add").click(() => {
        console.log("Add row");
    });
    add_td.append(add_btn);

    var remove_td = $("<td>");
    var remove_btn = $("<button>").html("Remove").click(() => {
        console.log("Remove row");
    });
    remove_td.append(remove_btn);

    var inner_div = $("<div>");
    inner_div.append(add_td);
    inner_div.append(remove_td);

    var button_tr = $("<tr>", {
        id: btn_row_id
    });
    button_tr.append(inner_div);
    table.append(button_tr);
}

$(document).ready(function(){
    $("#text_json").val(""); // Clear this out. Seems to want to keep values when refreshing
    $("#button_copy").click(() => {
        var text_json = $("#text_json").val();
        navigator.clipboard.writeText(text_json);
    });

    $("#button_generate").click(generate_sheet_json);

    $("#STR_SCORE_TXT").change(update_mods);
    $("#DEX_SCORE_TXT").change(update_mods);
    $("#CON_SCORE_TXT").change(update_mods);
    $("#INT_SCORE_TXT").change(update_mods);
    $("#WIS_SCORE_TXT").change(update_mods);
    $("#CHA_SCORE_TXT").change(update_mods);
    clear_abilities();

    clear_feats_table();
});