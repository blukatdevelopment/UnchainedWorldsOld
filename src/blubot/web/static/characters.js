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
const IMAGE = "image";

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

// Lists
const INVENTORY = "inventory";
const FEATS = "feats";
const SKILLS = "skills";

// Attacks
const ATTACKS = "attacks";
const ATTACK_NAME = "attack name";
const TO_HIT = "to hit";
const DAMAGE = "damage";
const DAMAGE_TYPE = "damage type";

const REQUIRED_FIELDS = [NAME, XP, HP, AC, CLASS, SIZE, CULTURE, SPEED, STAMINA_DICE, ARMOR_PROF, WEAPON_PROF, TOOL_PROF, LANGUAGES, PROF_BONUS, ABILITIES, SKILLS, INVENTORY, ATTACKS, SAVING_THROWS, FEATS];
const LIST_FIELDS = [FEATS, INVENTORY, SKILLS, SAVING_THROWS, LANGUAGES, ATTACKS];
// global variables
var g_feats_table;
var g_inventory_table;
var g_skills_table;
var g_saves_table;
var g_languages_table;
var g_attacks_table;


/*##############################################################################
#               ______      _        _     _     _                             #
#               |  _  \    | |      | |   (_)   | |                            #
#               | | | |__ _| |_ __ _| |    _ ___| |_                           #
#               | | | / _` | __/ _` | |   | / __| __|                          #
#               | |/ / (_| | || (_| | |___| \__ \ |_                           #
#               |___/ \__,_|\__\__,_\_____/_|___/\__|                          #
#                                                                              #
#   Get and load a list of text fields.                                        #
##############################################################################*/

function DataList(_table, _header, _blank_row, _table_name, _btn_row_id){
    var dl = {
        table: $("#"+_table),
        header: _header,
        blank_row: _blank_row,
        table_name: _table_name,
        btn_row_id: _table + "_btn"
    };

    dl.make_table = function(){
        dl.btn_row_id = dl.table_name + "_btn";
        dl.table.empty();
        dl.make_header_row();
        var row_data = [ dl.blank_row ];
        row_data.forEach((row) => {
            dl.add_data_row(row, dl.btn_row_id);
        });
        dl.make_table_buttons();
    }

    dl.make_header_row = function(){
        var header_txt = "<tr>";
        dl.header.forEach((column) => {
            header_txt += "<th>" + column + "</th>";
        });
        header_txt += "</tr>";
        dl.table.append("$" + header_txt);
    }

    dl.add_data_row = function(row){
        var button_row = $("#" + dl.btn_row_id);
        dl.table.remove(button_row);

        var row_tr = $("<tr>");
        var row_td = row_td = $("<td>");
        row.forEach(cell_data => {
            var row_input = $("<input>").attr({ type: 'text'}).val(cell_data);
            row_td.append(row_input);
        });
        row_tr.append(row_td);
        dl.table.append(row_tr);
        dl.table.append(button_row);
    }

    dl.remove_data_row = function(){
        if(dl.table.find("tr").length < 3){
            return;
        }
        dl.table.find("tr:nth-last-child(2)").remove();
    }

    dl.make_table_buttons = function(){
        var add_td = $("<td>");
        var add_btn = $("<button>").html("Add").click(() => {
            dl.add_data_row(dl.blank_row);
        });
        add_td.append(add_btn);

        var remove_td = $("<td>");
        var remove_btn = $("<button>").html("Remove").click(() => {
            dl.remove_data_row();
        });
        remove_td.append(remove_btn);

        var inner_div = $("<div>");
        inner_div.append(add_td);
        inner_div.append(remove_td);

        var button_tr = $("<tr>", {
            id: dl.btn_row_id
        });
        button_tr.append(inner_div);
        dl.table.append(button_tr);
    }
    // Only works for single column tables
    dl.get_data_list = function(){
        var rows = [];
        var last_index = dl.table.find("tr").length -1;
        dl.table.find("tr").each((index, record) => {
            if(index != 0 && index != last_index){
                var tr = $(record);
                var text = tr.find('td').find('input').val();
                if(text !== ''){
                    rows.push(text);    
                }
            }
        });
        return rows;
    }
    // Only works for single column tables
    dl.load_data_list = function(data_list){
        if(!Array.isArray(data_list)){
            return;
        }
        dl.make_table();
        if(data_list.length > 0){
            dl.remove_data_row();    
        }
        data_list.forEach((row) =>{
            var row_data = [];
            row_data.push(row);
            dl.add_data_row(row_data);
        });
    }
    dl.make_table();
    return dl;
}

/*##############################################################################
#                  ______      _        _____      _     _                     #
#                  |  _  \    | |      |  __ \    (_)   | |                    #
#                  | | | |__ _| |_ __ _| |  \/_ __ _  __| |                    #
#                  | | | / _` | __/ _` | | __| '__| |/ _` |                    #
#                  | |/ / (_| | || (_| | |_\ \ |  | | (_| |                    #
#                  |___/ \__,_|\__\__,_|\____/_|  |_|\__,_|                    #
#                                                                              #
#   Get and load a list of multi-column datarows                               #
##############################################################################*/

function DataGrid(_table, _header, _blank_row, _table_name, _btn_row_id){
    var dg = {
        table: $("#"+_table),
        header: _header,
        blank_row: _blank_row,
        table_name: _table_name,
        btn_row_id: _table + "_btn"
    };

    dg.make_table = function(){
        dg.btn_row_id = dg.table_name + "_btn";
        dg.table.empty();
        dg.make_header_row();
        var row_data = [ dg.blank_row ];
        row_data.forEach((row) => {
            dg.add_data_row(row, dg.btn_row_id);
        });
        dg.make_table_buttons();
    }

    dg.make_header_row = function(){
        var header_txt = "<tr>";
        dg.header.forEach((column) => {
            header_txt += "<th>" + column + "</th>";
        });
        header_txt += "</tr>";
        dg.table.append("$" + header_txt);
    }

    dg.add_data_row = function(row){
        var button_row = $("#" + dg.btn_row_id);
        dg.table.remove(button_row);

        var row_tr = $("<tr>");
        
        row.forEach(cell_data => {
            var row_td = row_td = $("<td>");
            var row_input = $("<input>").attr({ type: 'text'}).val(cell_data);
            row_td.append(row_input);
            row_tr.append(row_td);
        });
        dg.table.append(row_tr);
        dg.table.append(button_row);
    }

    dg.remove_data_row = function(){
        if(dg.table.find("tr").length < 3){
            return;
        }
        dg.table.find("tr:nth-last-child(2)").remove();
    }

    dg.make_table_buttons = function(){
        var add_td = $("<td>");
        var add_btn = $("<button>").html("Add Row").click(() => {
            dg.add_data_row(dg.blank_row);
        });
        add_td.append(add_btn);

        var remove_td = $("<td>");
        var remove_btn = $("<button>").html("Remove Row").click(() => {
            dg.remove_data_row();
        });
        remove_td.append(remove_btn);

        var inner_div = $("<div>");
        inner_div.append(add_td);
        inner_div.append(remove_td);

        var button_tr = $("<tr>", {
            id: dg.btn_row_id
        });
        button_tr.append(inner_div);
        dg.table.append(button_tr);
    }
    dg.get_data_rows = function(){
        var rows = [];
        var last_index = dg.table.find("tr").length -1;
        dg.table.find("tr").each((index, record) => {
            if(index != 0 && index != last_index){
                var row = [];
                var tr = $(record);
                var row_elements = tr.find('td').find('input').each((idx, rcrd) => {
                    var input = $(rcrd);
                    row.push(input.val());
                });
                rows.push(row);
            }
        });
        return rows;
    }
    dg.load_data_rows = function(data_rows){
        dg.make_table();
        dg.remove_data_row();
        data_rows.forEach((row) => {
            dg.add_data_row(row);
        });
    }
    dg.make_table();
    return dg;
}

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

function set_ability_score(ability, score){
    var id = get_ability_score_id(ability);
    $("#"+id).val(score);
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
    character = generate_table_fields(character);
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
    character[XP] = $("#XP_TXT").val();
    character[IMAGE] = $("#IMG_TXT").val();
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
    return character;
}

function generate_table_fields(character){
    character[FEATS] = g_feats_table.get_data_list();
    character[INVENTORY] = g_inventory_table.get_data_list();
    character[SKILLS] = g_skills_table.get_data_list();
    character[SAVING_THROWS] = g_saves_table.get_data_list();
    character[LANGUAGES] = g_languages_table.get_data_list();
    generate_attacks_data(character);
    return character;
}

function generate_attacks_data(character){
    var dict_rows = [];
    var raw_rows = g_attacks_table.get_data_rows();
    raw_rows.forEach((raw) => {
        var dict_row = {};
        dict_row[ATTACK_NAME] = raw[0];
        dict_row[TO_HIT] = raw[1];
        dict_row[DAMAGE] = raw[2];
        dict_row[DAMAGE_TYPE] = raw[3];
        dict_rows.push(dict_row);
    });
    character[ATTACKS] = dict_rows;
}

function set_up_tables(){
    g_feats_table = DataList(
        "FEATS_TABLE",
        ["Feats"],
        [""],
        "feats",
        ""
        );
    g_inventory_table = DataList(
        "INVENTORY_TABLE",
        ["Inventory"],
        [""],
        "inventory",
        ""
        );
    g_skills_table = DataList(
        "SKILLS_TABLE",
        ["Skills"],
        [""],
        "skills",
        ""
        );
    g_saves_table = DataList(
        "SAVES_TABLE",
        ["Saving throws"],
        [""],
        "saves",
        ""
        );
    g_languages_table = DataList(
        "LANGUAGES_TABLE",
        ["Languages"],
        [""],
        "languages",
        ""
        );
    g_attacks_table = DataGrid(
        "ATTACKS_TABLE",
        ["Attack", "To Hit", "Damage", "Damage Type"],
        ["", "", "", ""],
        "attacks",
        ""
        );
}


// Loads an existing sheet from a blob of json
function load_json(json){
    if(json == ''){
        json = '{}';
    }
    var character = JSON.parse(json);
    character = init_blank_char_fields(character);
    load_header_fields(character);
    load_abilities(character);
    load_stat_fields(character);
    load_proficiency_fields(character);
    load_table_fields(character);
}

function init_blank_char_fields(character){
    REQUIRED_FIELDS.forEach((field) => {
        if(typeof(character[field]) !== 'undefined'){
            // We're good to go
        }
        else if(LIST_FIELDS.indexOf(field) >= 0){
            character[field] = [];
        }
        else{
            character[field] = '';
        }
    });
    return character;
}

function load_abilities(character){
    var abilities = character[ABILITIES];
    set_ability_score(STRENGTH, abilities[0]);
    set_ability_score(DEXTERITY, abilities[1]);
    set_ability_score(CONSTITUTION, abilities[2]);
    set_ability_score(INTELLIGENCE, abilities[3]);
    set_ability_score(WISDOM, abilities[4]);
    set_ability_score(CHARISMA, abilities[5]);
}

function load_header_fields(character){
    $("#NAME_TXT").val(character[NAME]);
    $("#CLASS_TXT").val(character[CLASS]);
    $("#CULTURE_TXT").val(character[CULTURE]);
    $("#XP_TXT").val(character[XP]);
    $("#IMG_TXT").val(character[IMAGE]);
}

function load_stat_fields(character){
    $("#HP_TXT").val(character[HP]);
    $("#AC_TXT").val(character[AC]);
    $("#SIZE_TXT").val(character[SIZE]);
    $("#SPEED_TXT").val(character[SPEED]);
    $("#STAMINA_TXT").val(character[STAMINA_DICE]);
    $("#IMG_TXT").val(character[IMG]);
    $("#SENSES_TXT").val(character[SENSES]);
}

function load_proficiency_fields(character){
    $("#PROF_TXT").val(character[PROF_BONUS]);
    $("#WEAPONS_TXT").val(character[WEAPON_PROF]);
    $("#ARMORS_TXT").val(character[ARMOR_PROF]);
    $("#TOOLS_TXT").val(character[TOOL_PROF]);
}

function load_table_fields(character){
    g_inventory_table.load_data_list(character[INVENTORY]);
    g_feats_table.load_data_list(character[FEATS]);
    g_skills_table.load_data_list(character[SKILLS]);
    g_saves_table.load_data_list(character[SAVING_THROWS]);
    g_languages_table.load_data_list(character[LANGUAGES]);
    load_attacks_data(character[ATTACKS]);
}

function load_attacks_data(attacks){
    var list_rows = [];
    attacks.forEach((attack) => {
        var list_row = [];
        list_row.push(attack[ATTACK_NAME]);
        list_row.push(attack[TO_HIT]);
        list_row.push(attack[DAMAGE]);
        list_row.push(attack[DAMAGE_TYPE]);
        list_rows.push(list_row);
    });
    g_attacks_table.load_data_rows(list_rows);
}

$(document).ready(function(){
    $("#text_json").val(""); // Clear this out. Seems to want to keep values when refreshing
    $("#button_copy").click(() => {
        var text_json = $("#text_json").val();
        navigator.clipboard.writeText(text_json);
    });

    $("#button_load").click(() => {
        var text_json = $("#text_json").val();
        load_json(text_json);
    });

    $("#button_generate").click(generate_sheet_json);

    $("#STR_SCORE_TXT").change(update_mods);
    $("#DEX_SCORE_TXT").change(update_mods);
    $("#CON_SCORE_TXT").change(update_mods);
    $("#INT_SCORE_TXT").change(update_mods);
    $("#WIS_SCORE_TXT").change(update_mods);
    $("#CHA_SCORE_TXT").change(update_mods);
    clear_abilities();

    set_up_tables();
});