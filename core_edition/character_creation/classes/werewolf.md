```
################################################################################
#            _    _                             _  __                          #
#           | |  | |                           | |/ _|                         #
#           | |  | | ___ _ __ _____      _____ | | |_                          #
#           | |/\| |/ _ \ '__/ _ \ \ /\ / / _ \| |  _|                         #
#           \  /\  /  __/ | |  __/\ V  V / (_) | | |                           #
#            \/  \/ \___|_|  \___| \_/\_/ \___/|_|_|                           #
#                                                                              #
################################################################################
```
# Werewolf
There are legends of a curse that turns the innocent into bloodthirsty monsters by the light of the full moon. In some places, silvered weapons are put on display to defend against such monsters. Few know of the nature of this curse. Though some live largely unaware of it, or completely subordinate to the bestial urges of the monster's form, many others live with the curse and attempt to control it. This is the life of a werewolf.

## Hit points
Roll 3d4 and add your CON modifier three times(minimum 1HP). These are your starting hit points. Every time you gain a level, you may roll again and keep the total if it is higher.

## Stamina Die size
Your stamina die is a d4.

## Proficiencies
|:--------------|------------------------|
| Armor         | None                   |
|:--------------|------------------------|
| Weapons       | Simple                 |
|:--------------|------------------------|
| Tools         | None                   |
|:--------------|------------------------|
| Saving Throws | Constitution, Strength |
|:--------------|------------------------|

## Skills
You are proficient with the following:
- Hearing
- Smelling
- Tracking

## Starting equipment
- Dagger
- Backpack
- Waterskin
- Traveler's Clothes
- 10 rations
- 50ft rope
- bedroll
- Mess kit
- 10 torches
- pouch of 5GP

```
LVL = level
XP = total experience points needed for level
SD = Stamina Dice
Prof = proficiency bonus
```

| LVL |  XP    | SD|Prof |        Features                 |
|:----|--------|---|-----|---------------------------------|
|   1 |     0  | 2 | +1  | Werewolf Form, Controlled Shift |
|   2 |   300  | 4 | +1  | Howl                            |
|   3 |   900  | 6 | +2  | Charge                          |
|   4 |  1800  | 8 | +2  | Alpha Strike                    |
|   5 |  3600  |10 | +2  | Ability Score Increase          |
|   6 |  6100  |12 | +2  | Bloodlust                       |
|   7 |  9100  |14 | +3  | Werewolf Fortitude              |
|   8 | 13100  |16 | +3  | Extra Attack                    |
|   9 | 22600  |18 | +4  | Non-magical Immunity            |
|  10 | 44600  |20 | +4  | Ability Score Increase          |

## Features

### Werewolf Form
While shifted into your werewolf form, your hit die grows to a D10. You may expend one or more stamina dice when you shift, rolling and adding them to your werewolf form's maximum hit points. When your shift ends, you leave your werewolf form. This causes your maximum hit points to revert, and your hit points to reduce to 1. The following stat block is used when you shift.

```
Werewolf
Medium Monstrosity
HP: 20
AC: 13
Speed: 40ft
|STR|DEX|CON|INT|WIS|CHA|
| 18| 16| 12|  5|  5|  5|
Weak: slashing, bludgeoning, and piercing damage from silvered weapons
Pack Tactics: Your attacks against a target have advantage when an ally is within 5ft of it.
Resistance: slashing, bludgeoning, and piercing damage from non-magical, non-silvered weapons.
Attacks:
Jaws +4 1d10+4
Claws: +4 2d4+4 DC 14 CON save or contract malignant lycanthropy
```

### Controlled Shift
You've learned to control your shift into your shifter form. You may use your bonus action to expend a stamina die and shift into your shifter form at will. When you shift this way, you are in full control of yourself. That control lasts for 1 minute. When this time runs out, you may succeed a DC 12 wisdom save in order to maintain control and either remain in a controlled shift, or transform back into your humanoid form. You may consume a stamina die to remake this saving throw. If you fail, you lose control and your shift becomes an uncontrolled shift.

#### Uncontrolled shift
There are certain triggers that may cause you to involuntarily enter your shifter form. When you experience one of these triggers, you must make a wisdom save against it's DC(indicated in the table below) You may expend a stamina die to remake the throw once. If you fail this check, you involuntarily enter your shifter form. During an uncontrolled shift, you may remake the wisdom saving throw once each minute. Someone else designated by the keeper takes control of your character, applying logic from the uncontrolled shift behavior flowchart. If you succeed the check, you are immune to being triggered for the next hour.


| Uncontrolled shift triggers table   |
|:-------------------------------|----|
|            Trigger             | DC |
|:-------------------------------|----|
| See another wounded creature   | 10 |
| Smell scent of another's blood | 12 |
| See raw meat                   | 14 |
| Fall below 4 hit points        | 16 |
| Spend 6 seconds being grappled | 16 |
| Hearing the call of another    | 18 |
| werewolf                       |    |
| Witness a full moon            | 20 |

```
#################################
#    Uncontrolled Shift         #
#    Behavior Flowchart         #
#################################
#   |:------|                   #
#   | Start |                   #
#   |:--|---|                   #
#       |                       #
#  |:---V------|Yes|:---------| #
#  |           |   |          | #
#  | In active |:--> Fight    | #
#  |  Combat?  |   | Hostiles | #
#  |:---|------|   |:---------| #
#       | No                    #
#       |                       #
#  |:---V------|Yes|:---------| #
#  | Wounded   |   |Hunt Them | #
#  | Creature  |:-->          | #
#  | Nearby?   |   |:---------| #
#  |:---|------|                #
#       | No                    #
#  |:---V------|Yes             #
#  |  Fresh    |  |:----------| #
#  |  Meat     |:->  Feast    | #
#  |  Nearby?  |  |           | #
#  |:--|-------|  |:----------| #
#      |  No                    #
#      |                        #
#  |:--V------------|           #
#  | Call for       |           #
#  | Other          |           #
#  | shifters       |           #
#  |:--|------------|           #
#      |                        #
#  |:--V------------|           #
#  |                |           #
#  | Search for prey|           #
#  |                |           #
#  |:---------------|           #
#################################
```

### Howl
While in your werewolf form, expend one hit die and use your action to unleash a bloodcurdling howl. All werwolves within a mile radius are triggered by this. All creatures within a 10ft radius of you must succeed a WIS save or become frightened. They may remake the save at the end of their turn. The DC for the WIS save is equal to 8 + your proficiency bonus + CON. You also gain 2d8 temporary hit points when you howl.

#### Charge
You may expend two stamina dice to double your speed and make two additional attacks this turn. Your movement does not provoke attacks of opportunity for the rest of your turn.

### Alpha Strike
At level 4, when your bite attack hits, you may consume a stamina die to deal an extra 3d8 piercing damage.

### Bloodlust
At level 6, when you kill a creature with your jaws, you gain an action and a stamina die.

### Werewolf fortitude
At level 7, when you expend a stamina die to gain hit points at the start of a shift, you now gain 10 hit points instead of rolling.

### Extra atack
At level 8, in addition to any attacks you would normally make when you use the attack action in your werewolf form, you may make one additional attack.

### Non-magical immunity
At level 9, your werewolf form is immune to slashing, bludgeoning, and piercing damage from non-magical, non-silvered weapons. Your werewolf form has 45 maximum hit points now.