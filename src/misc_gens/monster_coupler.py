import random

# General
first = ["Tentacle Beast",
"Flesh Eaters",
"Chaos Shells",
"Infernoids",
"Mantis Man",
"Leech Man",
"Sentinel",
"Needlenose",
"Zombie",
"Skeletons",
"Skelemancer",
"Vampire",
"Slime(Any)",
"Rotheads",
"Shroom People",
"Nymph",
"Bandit(any)",
"Soldier (any)",
"Cultists(Any)",
"Dwarf Giants"]

# Specific
second = ["Wolf bat",
"Pincer Beast",
"Stone Scurrier",
"Giant Ant",
"Sha Karr",
"Mind Leech",
"Floating Eye",
"Giant Hand",
"Spindle Man",
"Muckbeast",
"Chameleoid",
"Raystalker",
"Manface silkworm",
"Marionette spider",
"Invisible Skulker",
"Changeling",
"Land Urchin",
"Carpet Worm",
"Swarm of Heart Worms",
"Pit Fisher",
"Hydra",
"Mimic",
"Shadow",
"Ghost / Banshee / Specter",
"Breath Skull",
"Grass Heap",
"Root Walkers",
"Fey Guardian",
"Arch Fey",
"Giant Crab",
"Snarl Beak",
"Huge Polar Bear",
"Sharp Tooth",
"Saber-toothed Tiger",
"Dire Wolf",
"Giant Spider",
"Brown Bear",
"Mountain Lion",
"Giant Leech",
"Featherclaws",
"Littlefoot",
"Sand Guardian",
"Flame Guardian",
"Grinders",
"Abyssal Giant",
"Bone Thresher",
"Gattogat",
"Vice",
"Imp",
"Regret",
"Devil Scribes",
"Hell Knight",
"Hell Hounds"]

def main():
    for i in range(40):
        print(f"{random.choice(first)} + {random.choice(second)} + {random.choice(second)}")

main()