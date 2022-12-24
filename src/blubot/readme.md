# Blubot
```
###############################################
#        xxxx                xxx              #
#        x   x              xx x              #
#        x x  x            x xx xx            #
#        x xx xx         xx xxx  x            #
#        xx x  xxxxxxxxx x x  x  x            #
#       x xxx              xxxx  x            #
#       x       x      x         x            #
#       x                       xx            #
#       x          xxxx         x             #
#        x          xx          x             #
#        x      x   xxx  xx     x             #
#         x     xxxxx xxxx     x              #
#         xx                  xx              #
#          xx               xxx   xxxxxx      #
#            xxxx        xxx     x     xx     #
#                xxx xxxxxxxx   xxxx    xx    #
#               xx           xxxx  xx    x    #
#              xx              xxxx     xx    #
#            xx                  xxxxxxxx     #
###############################################
```
Yo, this is Blukat! This is a discord bot in active development.
It's made mostly because other bots either have no character sheet management,
or are overly focused on proprietary game systems. Maybe I'll spruce up this doc
to include better detail for installing and using this thing. Maybe I'll add this
to a pile of abandoned projects. Only time will tell. `¯\_(ツ)_/¯`

## Player functionality
Here's some dev goals. Ideally, this will offer some Avrae-like commands and some
character sheet storage that doesn't 
- [DONE]Store, update, view character sheets as json
- [IN PROGRESS]Avrae-like commands to automate checks, saves, attacks, and manage resources(HP, stamina dice)
- A web page where players can view, edit, and save their character sheets

## Keeper functionality
These are more of stretch goals than anything, but heck, I'ma shoot for the stars!
- Commands to give info on weather, calendar date, current and upcoming events, active rumors in a given hex
- Commands to log character rewards, expenses, availability
- Command for generating a quest board prompts
- Command for encounter prompts


## Example Character Sheet
```
{
"name": "Envy",
"xp": 300,
"ac": 11,
"hp": 23,
"class": "scientist",
"size": "medium",
"culture": "Gold Robe",
"speed": "30ft",
"body type": "common",
"stamina dice": 4,
"armor proficiencies": "light",
"weapon proficiencies": "simple",
"tool proficiencies": "smith's tools",
"languages": ["common"],
"prof bonus": 1,
"abilities": [6, 12, 8, 20, 10, 15],
"saving throws": ["intelligence", "dexterity"],
"skills": {"investigation": "p"},
"inventory": ["common clothes", "bedroll", "dagger"],
"attacks": [
        {"attack name": "Claws", "to hit": -2, "damage": "1d4-3", "damage type": "slashing"},
        {"attack name": "Dagger", "to hit": 2, "damage": "1d4+1", "damage type": "piercing"}
    ]
}
```