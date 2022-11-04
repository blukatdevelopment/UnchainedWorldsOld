# Dungeon 1
Remember: Divide all gp, xp among adventurers evenly.
XP budget: 1200
GP budget: 300


## Level 1 (290xp)
```
E = entrance
D = stairs down
###############################
#       ┌─────┐ ┌─E──┐        #
#       │     ├─┤  1 │        #
#       │  2  │ │    ├────┐   #
#       └──┬──┘ └────┘    │   #
#          │              │   #
#        ┌─┴──┐ ┌────┐ ┌──┴─┐ #
#        │    ├─┤D   ├─┤  5 │ #
#        │ 3  │ │  4 │ │    │ #
#        └─┬──┘ └────┘ └──┬─┘ #
#          │              │   #
#        ┌─┴──┐ ┌─────┐   │   #
#        │    ├─┤     │   │   #
#        │  6 │ │  7 D├───┘   #
#        └─E──┘ └─────┘       #
###############################
```
### 1 

Exits
1. North Entrance
2. East
3. West

### 2 

Exits
1. South
2. East

### 3 
- 3 petty bandit (30xp)

Exits
1. North
2. East
3. South

### 4 
- 4 petty bandits (40xp)
- 3 bandits (75xp)
- 1 bandit captain (100xp)
Exits
1. West
2. East
3. Stairs Down (Level 2, room 8)

### 5 
- 2 petty bandit (20xp)
- 1 bandit (25xp)

Exits
1. North
2. West
3. South

### 6

Exits
1. North
2. East
3. South Entance

### 7 

Exits
1. West
2. East
3. Stairs Down (Level 2, room 8)

## Level 2 (905XP)

```
U = stairs up
###########################################
#          ┌────┐                         #
#          │  1 ├───────┐                 #
#          │    │       ├─────┐           #
#          └──┬─┘       │  2  │           #
#             │         │     │           #
#  ┌────┐     │         └───┬─┘           #
#  │ 4  │  ┌──┴─┐           │   ┌─────┐   #
#  │    ├──┤ 5  ├────┐      └───┤     │   #
#  └──┬─┘  │    │    ├────┐     │  3  │   #
#     │    └────┘    │ 6  │     │     │   #
#   ┌─┴──┐           │    │     └─┬───┘   #
#   │ 7  │           └─┬──┘       │       #
#   │    ├─────┐       │          │       #
#   └─┬──┘     │       │          │       #
#     │       ┌┴───┐   │    ┌─────┤       #
#     │       │ U  ├───┘ ┌──┤ 9   │       #
#     │       │  8 │     │  │     │       #
#     │       └─┬──┘     │  └─────┘       #
#     │         │        │                #
#   ┌─┴───┐     │     ┌──┴─┐              #
#   │ 10  │     │     │ 11 │              #
#   │     ├─────┘     │U   │              #
#   └┬────┘           └──┬─┘              #
#    │                   │                #
#    │      ┌─────────┐  │                #
#    │      │         │  │                #
#    └──────┤   12    ├──┘                #
#           │         │                   #
#           └─────────┘                   #
###########################################
```
### 1 
Exits
1. East
2. South

### 2
- 3 zombie runners(75xp)

Exits
1. Northwest
2. Southeast

### 3
- 4 zombies (100xp)

Exits
1. West
2. South

### 4
Exits
1. East
2. South

### 5
Exits
1. North
2. West
3. East

### 6
- Trap

Exits
1. Northwest
2. South

### 7
Exits
1. North
2. East
3. South

### 8
Exits
1. West
2. East
3. Stairs Up(Level 1, room 4)

### 9
- 3 zombies (75xp)
- 3 zombie runners(75xp)

Exits
1. North
2. South
3. East

### 10
Exits
1. North
2. East
3. South

### 11
Exits
1. North
2. South
3. Stairs Up(Level 1, room 7)

### 12
- Boss Monster

Exits
1. East
2. West

## Stat blocks

`Petty Bandit, XP: 10, HP: 10(2d4+3), AC: 11, [12, 12, 12, 10, 12, 12], Dagger +2 1d4+1 piercing, Sling +2 1d4+1 bludgeoning`

`Bandit, XP: 25, HP: 15(3d4+3), AC: 12(leather), [14, 12, 12, 10, 12, 12], Shortsword +4 1d6+2 piercing, Shortbow +4 1d6+1 piercing`

`Bandit Captain, XP: 100, HP: 36(3d10+6), AC: 13(hide), [16, 12, 12, 10, 12, 16], Shortsword +5 1d6+3 piercing`
- Multiattack: Captain can make two shortsword attacks

`Zombie, XP: 25, HP: 18(2d4+6), speed: 20ft, AC: 8, [14, 8, 14, 4, 4, 4], Bash +2 1d8+1 bludgeoning`
- Resistant: Non-magical physical, Weak: Radiant, Immune: Necrotic
- Undead Fortitude: When zombie falls to 0 hit points by damage other than fire
or radiant, they can make a con save to stay up with 1 hit point. The DC is half
the damage plus 10.

`Zombie Runner, XP: 25, HP: 18(2d4+6), speed: 20ft, AC: 8, [14, 8, 14, 4, 4, 4], Bite +2 1d4+1 piercing`
- Resistant: Non-magical physical, Weak: Radiant, Immune: Necrotic
- Corpse Run(1 use): As a reaction to bloodshed or a loud noise, the zombie moves up to 30ft toward the source.
- Multi-attack: Zombie may make two bite attacks
