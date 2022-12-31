import random

OBJECTIVES = [
"Return tribute",
"Emancipate farmstead",
"Assassinate officer",
"Deliver weapons",
"Liberate village",
"Secure weapons assets",
"Smuggle assets",
"Free prisoners",
"Negotiate Alliance",
"Provide aid"
]

def rebel_prompt():
    msg = '```json\n{\n'
    msg += f'\t"Objective": "{random.choice(OBJECTIVES)}",\n'
    msg += f'\t"Reward": "50gp, 1 Rebel Renoun"\n'
    msg += "}```"
    return msg