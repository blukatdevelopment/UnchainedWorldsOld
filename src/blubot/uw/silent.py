import random

OBJECTIVES = [
"Assassinate researcher",
"Sabotage research project",
"Steal artifact",
"Steal prototype",
"Destroy artifact",
"Destroy prototype",
"Kidnap researcher",
"Alter records",
"Intercept caravan"
]

TECH_INVOLVED = [
"Aircraft",
"Land vehicle",
"Spacecraft",
"Satellite",
"Blaster",
"Shield generator",
"Food Replicator",
"Computer",
"Communicator",
"Induced Corruption",
"Forgelings",
"Impulse Engine",
"Soul Cage",
"Beam",
"Medical Scanner",
"Metal Interleaver",
"Dragon armor",
"Orbital Cannon",
"Planet buster",
"Radiant Sword",
"Dimension Gate",
"Fiendish Specimen",
"Giant Specimen",
"God Bone",
"Mind Machine Interface",
"Dragon Bone",
"Hell Steel"
]

def silent_prompt():
    msg = '```json\n{\n'
    msg += f'\t"Objective": "{random.choice(OBJECTIVES)}",\n'
    msg += f'\t"Tech Involved": "{random.choice(TECH_INVOLVED)}",\n'
    msg += f'\t"Reward": "200gp, 1 Silent Order Renoun"\n'
    msg += '}```'
    return msg