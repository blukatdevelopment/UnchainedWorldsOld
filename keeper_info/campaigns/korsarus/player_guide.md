# Quickstart Guide

## Your first character
Your first character starts as a Commoner from the Soot culture. This will get you into the action quickly. As you interact with the world, you'll unlock new classes, cultures, and other character options.

### Your backstory
You were born and raised in the filthy slums of the copper ring of Korsarus City. Whether your old life involved shoveling maneur, begging on the street, or picking pockets is irrelevant. You've got nothing to show for that life, and are taking, and nothing to lose by abandoning it for a life of adventuring.

### Your stat block
You can use the `/character update` command and use the stat block below. You might want to change the name from "Fresh Meat", though.
```
{
"name": "Fresh Meat",
"xp": 0,
"ac": 10,
"hp": 5,
"class": "Commoner",
"size": "medium",
"culture": "Soot",
"speed": "30ft",
"body type": "common",
"stamina dice": 0,
"armor proficiencies": "",
"weapon proficiencies": "",
"tool proficiencies": "",
"languages": ["common"],
"prof bonus": 0,
"abilities": [10, 10, 10, 10, 10, 10],
"saving throws": [],
"skills": {},
"inventory": ["common clothes", "club"],
"attacks": [
        {"attack name": "Unarmed", "to hit": 0, "damage": "1", "damage type": "bludgeoning"},
        {"attack name": "Club", "to hit": 0, "damage": "1d4", "damage type": "bludgeoning"}
    ]
}
```