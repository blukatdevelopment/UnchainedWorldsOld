# Quickstart Guide

## Your first character
Your first character starts as a Commoner from the Soot culture. This will get you into the action quickly. As you interact with the world, you'll unlock new classes, cultures, and other character options. Your appearance can be your choice of human or beast folk, as described below.

### Human
Humans are the most common humanoid by far, and they vary heavily. While some humans stand eight feet in height, and others stand under four, it's most common for humans to sand between five and six feet tall. Rarely, humans have elongated ears, or those of a beast coupled with a similar tail. The most common complexion for human ranges from pink, yellow, tan, and brown. Green, blue, and crimson skin is exotic, but not unheard of. Humans were originally created by Bimros in an attempt to populate the world with worshippers.

### Beast folk
Beast have a vaguely humanoid frame, but their features are that of beasts. Fur, scales, feathers, and leathery hides are the norm for beast folk.

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