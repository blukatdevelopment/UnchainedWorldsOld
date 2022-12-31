import random

# TODO: Add specific Hex from Giant's Playground for some of the objectives

OBJECTIVES = [
"Recon",
"Patrol Road",
"Escort Caravan",
"Repel Attack",
"Redirect Attackers",
"Eliminate rebel leader",
"Secure Location",
]

def scouts_prompt():
    msg = '```json\n{\n'
    msg += f'\t"Objective": "{random.choice(OBJECTIVES)}",\n'
    msg += f'\t"Reward": "150gp, 2 Omaria Renoun"\n'
    msg += "}```"
    return msg