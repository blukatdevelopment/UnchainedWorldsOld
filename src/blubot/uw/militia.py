import random

OBJECTIVES = [
'Monster hunt',
'Monster nest',
'Monster recovery',
'Bounty recovery',
'Asset Recovery',
'Defend the asset',
'Retake the farmstead',
'Collect Tribute from the farmstead',
'Raize the farmstead',
'Clear the bandit hideout',
'Clear the cultists',
'Locate the hidden rebel base',
'Discover and apprehend the killer']

TARGET_ADJECTIVES = [
'angry',
'hungry',
'scared',
'prepared',
'unprepared',
'innocent',
'reinforced',
'aggressive',
'proactive',
'defensive',
'humorless',
'skilled',
'magical',
'rare',
'plentiful'
]

COMPLICATIONS = [
'Rebel ambush',
'Monster attack',
'Diversion',
'Staff injury',
'Mutiny',
'Bad intel',
'Bad gear',
'Corrupt staff'
]

def militia_prompt():
    msg = '```json\n{\n'
    msg += f'\t"Objective": "{random.choice(OBJECTIVES)}",\n'
    msg += f'\t"Target adjective": "{random.choice(TARGET_ADJECTIVES)}",\n'
    msg += f'\t"Complications": "{random.choice(COMPLICATIONS)}",\n'
    msg += f'\t"Reward": "10gp, 1 Omaria Renoun"\n'
    msg += '}```'

    return msg