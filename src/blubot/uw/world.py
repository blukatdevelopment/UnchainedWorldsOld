# This is set up with data from the crucible setting and korsarus campaign. :3

DIVINE_AGE = "Divine Age"
AGE_OF_DRAGONS = "Age of Dragons"
TITAN_AGE = "Titan Age"
AGE_OF_MAN = "Age of man"
ERA_MAP = {
    1: DIVINE_AGE,
    2: AGE_OF_DRAGONS,
    3: TITAN_AGE,
    4: AGE_OF_MAN
}

GIDURSUS = "Gidursus"
BIMRAS = "Bimras"
ICEFALL = "Icefall"
FIRST_SEED = "First Seed"
GLASS_EYE = "Glass Eye"
COENTAS = "Coentas"
GIGTEXAS = "Gigtexas"
LAST_SEED = "Last Seed"
SOLUSMUS = "Solusmus"
HARVEST = "Harvest"
LEAFALL = "Leafall"
COENTOS = "Coentos"
MONTH_MAP = {
    1:  GIDURSUS,
    2:  BIMRAS,
    3:  ICEFALL,
    4:  FIRST_SEED,
    5:  GLASS_EYE,
    6:  COENTAS,
    7:  GIGTEXAS,
    8:  LAST_SEED,
    9:  SOLUSMUS,
    10: HARVEST,
    11: LEAFALL,
    12: COENTOS
}

ERA = "era"
YEAR = "year"
MONTH = "month"
DAY = "day"
WINTER = "winter"
SPRING = "spring"
SUMMER = "summer"
AUTUMN = "autumn"
SEASON_MAP = {
    1:  WINTER,
    2:  WINTER,
    3:  WINTER,
    4:  SPRING,
    5:  SPRING,
    6:  SPRING,
    7:  SUMMER,
    8:  SUMMER,
    9:  SUMMER,
    10: AUTUMN,
    11: AUTUMN,
    12: AUTUMN
}

MOONDAY = "Moonday"
ARROWDAY = "Arrowday"
LEAFDAY = "Leafday"
HAMMERDAY = "Hammerday"
COINDAY = "Coinday"
CLAWDAY = "Clawday"
SUNDAY = "Sunday"
DAY_MAP = {
    1: MOONDAY,
    2: ARROWDAY,
    3: LEAFDAY,
    4: HAMMERDAY,
    5: COINDAY,
    6: CLAWDAY,
    7: HAMMERDAY
}

DAY_FANCY_MAP = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelth",
    13: "thirteenth",
    14: "fourteenth",
    15: "fifteenth",
    16: "sixteenth",
    17: "seventeenth",
    18: "eighteenth",
    19: "nineteenth",
    20: "twentieth",
    21: "twenty-first",
    22: "twenty-second",
    23: "twenty-third",
    24: "twenty-fourth",
    25: "twenty-fifth",
    26: "twenty-sixth",
    27: "twenty-seventh",
    28: "twenty-eighth",
    29: "twenty-ninth",
    30: "thirtieth"
}

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

def get_current_date():
    return {
        ERA: 4,
        YEAR: 112,
        MONTH: 2,
        DAY: 24
    }

def format_date(date):
    era = date[ERA]
    year = date[YEAR]
    month = MONTH_MAP[date[MONTH_MAP]]
    day = DAY_FANCY_MAP[date[DAY]]
    return f"{day} {month}, year {year} of the {era}."

def today_date():
    date = get_current_date()
    return f"{date[MONTH]}/{date[DAY]}/{date[YEAR]}"

def get_status(year, month, day, hex):
    date = get_current_date()
    info = format_date(date)
    return info

def generate_encounter(date, location):
    return "Something happens, I guess."