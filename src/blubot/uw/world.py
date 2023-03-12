# This is set up with data from the crucible setting and korsarus campaign. :3
import datetime
import json
import random

WORLD_ID = 1
WORLD_START_DATE = "114/01/01"
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
WORLD_ERA = AGE_OF_MAN

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
DAYS = "days"
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
    28: "twenty-eighth"
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

# World status info
IRL_DATE = "irl date"
IN_WORLD_DATE = "world date"
WORLD_STATUS_FIELDS = [IRL_DATE, IN_WORLD_DATE]

# Calendar day data
WIND = "wind"
NO_WIND = 0
WEAK_WIND = 1
STRONG_WIND = 2 
PRECIPITATION = "precipitation"
NO_PRECIPITATION = 0
SCATTERED_PRECIPITATION = 1
HEAVY_PRECIPITATION = 2
EVENTS = "events"

# Holidays
HUMANS_DAY = "Human's Day"
BEASTFOLK_DAY = "Beastfolk Day"
COENTAS_DAY = "Coentas Day"
COENTOS_DAY = "Coentos Day"
GIANTS_REST = "Giant's Rest"
GIANTS_FEAST = "Giant's Feast"
GIANTS_THANKS = "Giant's thanks"
NEW_YEARS_EVE = "New Year's Eve"
NEW_YEARS_DAY = "New Year's Day"
ANVIL_DAY = "Anvil Day"
HAMMER_DAY = "Hammer Day"
GOLD_COINDAY = "Gold Coinday"
SEVERING_DAY = "Severing Day"
SPIRITS_NIGHT = "Spirits Night"
COENTAS_FEAST = "Coenta's Feast"
CHAOS_DAY = "Chaos Day"
COENTOS_FAST = "Coento's Fast"
COENTOS_FEAST = "Coento's Feast"
KORDMAS = "Kordmas"
BRIGHT_SUNDAY = "Bright Sunday"
KINGS_DAY = "King's Day"
SWORDS_DAY = "Swords Day"
GREEN_DAY = "Green Day"
TITANFALL = "Titanfall"
SLAYERS_DAY = "Slayers Day"
EXHMAS = "Exhmas"
HOLIDAYS_LIST = [HUMANS_DAY, BEASTFOLK_DAY, COENTAS_DAY, COENTOS_DAY, GIANTS_REST, GIANTS_FEAST, GIANTS_THANKS, NEW_YEARS_EVE, NEW_YEARS_DAY, ANVIL_DAY, HAMMER_DAY, GOLD_COINDAY, SEVERING_DAY, SPIRITS_NIGHT, COENTAS_FEAST, CHAOS_DAY, COENTOS_FAST, COENTOS_FEAST, KORDMAS, BRIGHT_SUNDAY, KINGS_DAY, SWORDS_DAY, GREEN_DAY, TITANFALL, SLAYERS_DAY, EXHMAS]
HOLIDAY_DATE_MAP = {
    HUMANS_DAY: "6/1",
    BEASTFOLK_DAY: "7/1",
    COENTAS_DAY: "6/1",
    COENTOS_DAY: "12/1",
    GIANTS_REST: "7/14",
    GIANTS_FEAST: "8/14",
    GIANTS_THANKS: "9/14",
    NEW_YEARS_EVE: "12/28",
    NEW_YEARS_DAY: "1/1",
    ANVIL_DAY: "2/25",
    HAMMER_DAY: "2/26",
    GOLD_COINDAY: "11/27",
    SEVERING_DAY: "12/15",
    SPIRITS_NIGHT: "10/25",
    COENTAS_FEAST: "11/28",
    CHAOS_DAY: "4/3",
    COENTOS_FAST: "5/21",
    COENTOS_FEAST: "5/28",
    KORDMAS: "2/12",
    BRIGHT_SUNDAY: "9/7",
    KINGS_DAY: "7/12",
    SWORDS_DAY: "8/10",
    GREEN_DAY: "9/1",
    TITANFALL: "5/3",
    SLAYERS_DAY: "4/12",
    EXHMAS: "1/20"
}

def get_current_date(db):
    status = db.get_world_status(WORLD_ID)
    status = json.loads(status)
    world_date = string_to_world_date(status[IN_WORLD_DATE])
    irl_start = datetime.datetime.strptime(status[IRL_DATE], "%Y/%m/%d").date()
    irl_today = datetime.date.today()
    delta = irl_today - irl_start
    year = world_date[YEAR]
    month = world_date[MONTH]
    day = world_date[DAY]
    (year, month, day) = advance_date_by_days(year, month, day, delta.days)
    return {
        ERA: WORLD_ERA,
        YEAR: year,
        MONTH: month,
        DAY: day
    }

def world_date_to_string(date_object):
    return f"{date_object[YEAR]}/{date_object[MONTH]}/{date_object[DAY]}"

def string_to_world_date(date_string):
    (year, month, day) = date_string.split("/")
    return {
        ERA: WORLD_ERA,
        YEAR: int(year),
        MONTH: int(month),
        DAY: int(day)
    }

def format_date(date):
    era = date[ERA]
    year = date[YEAR]
    month = MONTH_MAP[date[MONTH]].capitalize()
    day = DAY_FANCY_MAP[date[DAY]].capitalize()
    return f"{day} of {month}, year {year} of the {era}."

def today_date(db):
    date = get_current_date(db)
    return f"{date[MONTH]}/{date[DAY]}/{date[YEAR]}"

def is_valid_world_date(date_string):
    start_date = string_to_world_date(WORLD_START_DATE)
    date_parts = date_string.split("/")
    if len(date_parts) != 3:
        return False
    for part in date_parts:
        if not part.isdigit():
            return False
    if start_date[YEAR] > int(date_parts[0]):
        return False
    return True

def get_status(db, year, month, day, hex):
    date = get_current_date(db)
    info = format_date(date)
    return info

def generate_encounter(date, location):
    return "Something happens, I guess."

def advance_date_by_days(year, month, day, days):
    for i in range(days):
        (year, month, day) = next_date(year, month, day)
    return (year, month, day)

def next_date(year, month, day):
    day += 1
    if day > 28:
        day = 1
        month += 1
    if month > 12:
        month = 1
        year += 1
    return (year, month, day)

def get_wind():
    roll = random.randint(1, 6)
    if roll == 1:
        return STRONG_WIND
    elif roll == 2:
        return WEAK_WIND
    return NO_WIND

def get_precipitation():
    roll = random.randint(1, 6)
    if roll == 1:
        return HEAVY_PRECIPITATION
    elif roll < 4:
        return SCATTERED_PRECIPITATION
    return NO_PRECIPITATION

def generate_random_calendar_day_data(month, day):
    data = {}
    data[PRECIPITATION] = get_precipitation()
    data[WIND] = get_wind()
    events = get_day_events(month, day)
    if len(events) > 0:
        data[EVENTS] = events
    return data

def get_day_events(month, day):
    events = []
    date_key = f"{month}/{day}"
    for holiday in HOLIDAYS_LIST:
        #print(f"Comparing {date_key} with {HOLIDAY_DATE_MAP[holiday]}")
        if HOLIDAY_DATE_MAP[holiday] == date_key:
            events.append(holiday)
    return events

def populate_calendar(db):
    print("Populating calendar")
    db.clear_entire_calendar()
    set_world_status(db)
    year = 114
    month = 1
    day = 1
    for i in range(3360):
        day_data = generate_random_calendar_day_data(month, day)
        db.insert_calendar_day_data(year, month, day, json.dumps(day_data))
        print(f"Date {year}/{month}/{day}")
        (year, month, day) = next_date(year, month, day)
    print("Calendar population complete")

def set_world_date(db, world_date):
    return set_world_status(db, world_date)

def set_world_status(db, world_date=WORLD_START_DATE):
    status = {}
    status[IRL_DATE] = datetime.date.today().strftime("%Y/%m/%d")
    status[IN_WORLD_DATE] = world_date
    data = json.dumps(status)
    db.delete_world_status(WORLD_ID)
    db.insert_world_status(WORLD_ID, data)

def update_world_status(db, status):
    json_data = json.dumps(status)

def get_world_status(db, date):
    if date == "today":
        date = get_current_date(db)
    else:
        date = string_to_world_date(date)

    json_data = db.get_world_status(WORLD_ID)
    status = json.loads(json_data)
    
    day_data = json.loads(db.get_calendar_day_data(date[YEAR], date[MONTH], date[DAY]))
    week = get_next_week_of_data(db, date)
    upcoming_events = get_upcoming_events(week)
    msg = format_date(date) + "\n"
    msg += get_weather_description(day_data, date) + "\n"
    if EVENTS in day_data:
        msg += "Today's events:\n"
        for event in day_data[EVENTS]:
            msg += f"\t-{event}\n"
    if len(upcoming_events) > 0:
        msg += "Upcoming events:\n"
        #print(f"Upcoming events {upcoming_events}")
        for event in upcoming_events:
            #print(f"Event: {event}")
            msg += f"\t-{event}\n"
    return msg

def get_upcoming_events(week):
    events = []
    for day in week:
        if EVENTS in day:
            day_events = day[EVENTS]
            for event in day_events:
                days = day[DAYS]
                events.append(f"{event}({days} days)")
    return events

def get_next_week_of_data(db, date):
    week = []
    year = date[YEAR]
    month = date[MONTH]
    day = date[DAY]
    for i in range(7):
        (year, month, day) = next_date(year, month, day)
        data = json.loads(db.get_calendar_day_data(year, month, day))
        data[DAYS] = i+1
        week.append(data)
    return week

def get_weather_description(day_data, date):
    print(f"day_data {day_data}")
    month = date[MONTH]
    season = SEASON_MAP[month]
    wind = day_data[WIND]
    prec = day_data[PRECIPITATION]
    if wind == NO_WIND and prec == NO_PRECIPITATION:
        return f"A sunny {season} day."

    msg = ""
    if wind == STRONG_WIND:
        msg += "Howling"
    elif wind == WEAK_WIND:
        msg += "Breezy"
    if prec == HEAVY_PRECIPITATION:
        msg += " snow storm." if season == WINTER else "thunder storm"
    if prec == SCATTERED_PRECIPITATION:
        msg += " scattered snow showers." if season == WINTER else "scattered showers."
    if prec == NO_PRECIPITATION:
        msg += f", sunny {season} day."
    return msg