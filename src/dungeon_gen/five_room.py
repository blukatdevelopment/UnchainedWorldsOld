#!/usr/bin/python3
import random

THEMES = ["Earth",
"Fire",
"Wind",
"Water",
"Light",
"Shadow",
"Iron",
"Glass",
"Wood",
"Stone",
"Sand",
"Clay",
"Arcane",
"Necromancy",
"Fiendish",
"Elemental",
"Divine",
"Wild Magic",
"Fear",
"Revenge",
"Secrecy",
"Protection",
"Theft",
"Sacrifice",
"Mushroom",
"Thread",
"Crystal",
"Scroll",
"Glitter",
"Mirror",
"Howling",
"Gnashing",
"Stomping",
"Scraping",
"Gliding",
"Squirming"]

def print_roll(title, table):
	string = title + ": " + random.choice(table)
	print(string)

def choose_two_unique(table):
	first = random.choice(table)
	second = ""
	done = False
	while not done:
		second = random.choice(table)
		if first != second:
			return (first, second)

def choose_x_unique(x, table):
	selected = []
	selected.append(random.choice(table))
	while len(selected) < x:
		choice = random.choice(table)
		if choice not in selected:
			selected.append(choice)
	return selected

print_roll("Entrance",[
	"Guardian monster",
	"Hostile patrol or ambush",
	"Plot token or MacGuffin required to enter",
	"Proof of dedication",
	"Dangerous terrain or environment",
	"Entrance is secret or hidden"])

print_roll("Puzzle",[
	"Trial of dedication",
	"Traps set to kill intruders",
	"Very deadly traps with hints",
	"Temptation or gambling opportunity",
	"A choice between two dangerous obstacles",
	"NPC holding critical resource"])

print_roll("Setback",[
	"Deadend with deady trap(such as crushing walls)",
	"Path with planned ambush",
	"Evidence the reward differs from what is expected",
	"A friendly NPC defects or reveals hidden alterior motives",
	"An inactive element(traps, enemies) of the dungeon actives",
	"An obstacle is created, blocking exit"])

print("Battle:")

print_roll("\tEnemies",[
	"Boss buffed by minions",
	"Boss buffs minions",
	"Minion spawners",
	"Mooks, strikers, glass cannons",
	"Solo boss",
	"Adventuring party equivalent"])

print_roll("\tTerrain",[
	"Connected platforms over hazard",
	"Standing and fallen pillars",
	"Fragile/Unstable surface",
	"Riddled with hazards(traps, fire, dripping acid, poison gas etc)",
	"Varied elevation platforms",
	"connected chambers with narrow connections"])

print_roll("\tTimed Threat",[
	"Hazard appears",
	"Existing hazard intensifies",
	"Buff for enemies",
	"Debuff for party",
	"Terrain changes dramatically",
	"Reinforcements arrive"])

print_roll("Reward",[
	"MacGuffin used to access new location/faction",
	"Hoard of riches",
	"Powerful magic item",
	"Revelation or mystery",
	"Paid objective for patron",
	"MacGuffin for heroic deed(such as finding cure, freeing prisoners)"])

print_roll("Structure",[
	"Railroad: E -> P -> S -> B -> R",
	"Rooster:\n     ---> P\n     |\nE -> S -> B\n     |\n     ---> R",
	"Cross:\n    P\n    |\nS - E - B\n    |\n    R",
	"Flying V:\nB        R\n  S    P\n     E",
	"Decision:\n            ---> B\nE -> P -> S |\n            ---> R",
	"Wrong way: S-E-P-B-R"])

print("Jacquays the structure:")
print_roll("\tConnection 1",[
	"Hidden path",
	"Obstructed path",
	"Visible path ",
	"Path with one side hidden/obstructed, one side visible"])
rooms = choose_two_unique(["Entrance", "Puzzle", "Setback", "Battle", "Reward", "Hidden Room"])
print("\tbetween {} and {}".format(rooms[0], rooms[1]))

print_roll("\tConnection 2",[
	"Hidden path",
	"Obstructed path",
	"Visible path ",
	"Path with one side hidden/obstructed, one side visible"])
rooms = choose_two_unique(["Entrance", "Puzzle", "Setback", "Battle", "Reward", "Hidden Room"])
print("\tbetween {} and {}".format(rooms[0], rooms[1]))

print("Themes(Choose 2):")
five_themes = choose_x_unique(5, THEMES)
for i in range(5):
	print("\t{}. {}".format(i+1, five_themes[i]))