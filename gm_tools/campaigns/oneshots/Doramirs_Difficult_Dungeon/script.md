# Doramir's Difficult Dungeon
During the days of the Dwarven empire, a powerful dwarven king offered a
competition among the magical artisans of the time to construct a tomb
challenging enough to keep all but the most worthy from reaching his axe. Rather
than fading into obscurity, Doramir's tomb became famous even far into the days
of the human empires, known as Doramir's Difficult Dungeon.

## Room 1 Switches
```

 ┌───────────x─────────────┐
 │           B             │
 │   ┌───┐         ┌───┐   │
 │   │ A │         │ A │   │
 │   └───┘         └───┘   │
 │C                      C │
 │                         │
 │                         │
 │                         │
 │                         │
 │C                      C │
 │   ┌───┐         ┌───┐   │
 │   │ A │         │A  │   │
 │   └───┘         └───┘   │
 │                         │
 └────────────x────────────┘
A: Pillar
B: Switches
C: Wall

```
The first chamber is a large cube with four switches in the on position, giving
off a heatless blue fire. Beside them is a large stone button. Inscribed above
them are the only instructions in Dwarven: "What's 2+2?"

Various outcomes:
0100 = Blue crystal appears, the Northern wall opens
1000 = The room begins to fill with noxious gas. Everyone is poisoned for 1 hour
1011 = roll twice for monsters
Anything else = roll for monsters

```
+------+--------------------+
| Roll |      Monsters      |
+------+--------------------+
|    1 | 1d6 skeletons      |
|    2 | Bone heap          |
|    3 | 1d4 breath skulls  |
|    4 | 1d4 bone gauntlets |
+------+--------------------+
```

## Room 2 Wheel
```



                 ┌────┐
                 │    │
      ┌────┐     │    │
      │    │     └───▲┘
      │    │         │
      └──▲─┘         │
         │    ┌────┐ │  ┌────┐
         └────┤    ├─┘  │    │
              │    │    │    │
              └──▲─┘    └──▲─┘
                 │         │
      ┌────┐     │ ┌────┐  │
      │    │     └─┤    ├──┘
      │    │       │    │
      └─▲──┘       └──▲─┘
        │    ┌─x──┐   │
        └────┤ A  ├───┘
             │    │
             └──x─┘
A: Entrance
```
The room has an inscription on the northern wall above a wheel. The wheel
has the numbers 1-6 on it, and an arrow to it's left to allow the adventurers
to select it. The inscription reads. "Count the leaves"
The answer is 4. 
If the party answers incorrectly once, the arrow turns red and they'll hear a
click and gates rise up on the West and East entrances to the room. Monsters
will begin to gather at those gates. If they answer wrong the second time,
the gates fall. Defeating the monsters or answering correctly will cause a green
gem to appear and the Northern door to open.

Monsters on left:
- 2d10 skeletons
- 1 Skelemancer
Monsters on right:
- 1d4 reapers
- 1d10 Breath Skulls (acid)

## Room 3 Library
```

 ┌───────────────x──────────────────┐
 │                                  │
 │                                  │
 │                                  │
 │  ┌─┐ ┌─┐ ┌─┐          ┌───┐      │
 │  │ │ │ │ │ │          │   │      │
 │  │ │ │ │ │ │          └───┘      │
 │  │ │ │ │ │ │                     │
 │  │ │ │ │ │ │                     │
 │  │ │ │ │ │ │          B  ┌───┐   │
 │  │ │ │ │ │ │             │   │   │
 │  │ │ │ │ │ │             └───┘   │
 │  │ │ │ │ │ │        ┌───┐        │
 │  │ │ │ │ │ │        │   │        │
 │  │ │ │ │ │ │        └───┘        │
 │  └─┘ └─┘ └─┘                     │
 │     A                            │
 │                                  │
 │                         ┌────────┤
 │                         │┼───────┤
 │                         ││       │
 │                         ││  C    │
 │                         ││       │
 └────────────────x────────┴┴───────┘

A: Bookshelves
B: Study Tables
C: Checkout Desk
```
This library is full of ghosts checking out and reading various books.
One ghost with bright yellow eyes will stop the party.
"To get through here, you will need to get through me. Instead of a fight,
you may answer my riddles three. But a warning to the slow and simple of mind,
you'll have one minute to answer, and I am not kind."

He gives three riddles. Each time the party answers one incorrectly,
he copies himself and a duplicate floats to his side. The party will fight
after the three riddles unless they answer every riddle correctly.

"The midnight code is moon square moon. What is the noon code?"
->"Sun square sun"

"Humans are featherless bipeds. Is a plucked chicken a human?"
"Yes" -> "Of course it's not!"
"No" -> "Of course it is! Weren't you listening?"
"With that definition, yes." -> "Correct"

"Three dogs have four hats. Four cats have six hats. Nine birds have how many
hats?" -> "10 hats"

After fighting or solving the riddling ghost, a yellow gem appears and the door
to the North opens.

## Room 4: Tiles
```


   ┌───────────────────────────────────────┬─────────────────────────────────┬─────────────────────────────────┐
   │  A                                    │  B                              │  C                              │
   │                                       │                     x           │                                 │
   │                                       │     xxx            xxxx         │   xx                    xx      │
   │          xxxx        xxx              │   xxxxxxx         xxxxxxx       │    xx                 xxx x     │
   │          xxxxx       xxx              │ xx    xx           xxx  xx      │    x x               xx    x    │
   │             x                         │                                 │    x  x x          xx      xx   │
   │                          x            │                                 │    xxx   xx      xxx     xx     │
   │         x                xx           │               xxxxxx            │      xxxxxxx     x     xxx      │
   │          x               xx           │         x x x       xx          │                  xxxxxx    x    │
   │          x            xxxx            │        xx             xx        │                           xx    │
   │           xx       xxxx               │       x                x        │   xx                     xx     │
   │            xxxxxxxx                   │      x                 xx       │    xx                 xxxx      │
   │                                       │                                 │      xxxxxx xxx xxxxxxx         │
   │                                       │                                 │                                 │
   │                                       │                                 │                                 │
   ├───────────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
   │                                       │                                 │                                 │
   │D                                      │ E           xx                  │F                                │
   │                                       │       xx   xxxx                 │                                 │
   │                        xxxxxxxxxx     │       xxx  x  x     xxx         │              xx                 │
   │                      xxx              │       x x  x  x    xx x         │             x  x                │
   │                    xx                 │       x  xxx  x    x  x         │            x    x               │
   │                   x                   │       x  xx   x  xx   x         │           x     x               │
   │                 x x                   │       x   x   x x     x         │          x       x              │
   │                x                      │       x       xxx     x         │         x         x             │
   │               xxxxxxxxxx              │       x       xx      x         │                   x             │
   │            xx                         │       x               x         │      x x           x            │
   │         xxx                           │       x               x         │      x             x            │
   │       xxx                             │       x               x         │    xx               x           │
   │      xxxxxxxxxxx xxxxxx               │       xx             x          │   xx                 x          │
   │                                       │        xx           xx          │   xxx x   x x x x xxxxx         │
   │                                       │          xxxxxxxxxxx            │                                 │
   │                                       │                                 │                                 │
   │                                       │                                 │                                 │
   │                                       │                                 │                                 │
   ├───────────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
   │                                       │                                 │                                 │
   │G                                      │ H                               │ I                               │
   │                                       │                                 │                                 │
   │                                       │                                 │              x                  │
   │             xxxxxxxxxxxx              │                                 │             x xx                │
   │            xx          xxxx           │                                 │             x   xx              │
   │           xx              xx          │       xxxx       xxxxx          │            x      x             │
   │           x                xx         │       xxxx       xxxxxx         │                    xx           │
   │           x                 x         │        xx         xxxx          │           x         x           │
   │           x                xx         │                                 │         xx           xx         │
   │           xx               xx         │                                 │         xxxx xx x x xxxxx       │
   │            xx              xx         │                       x         │                 x               │
   │             xxx          xx           │    x         xx       xx        │                 x               │
   │               xxxxxxxxxxx             │    x         xx        x        │                 x               │
   │                                       │    x       xx  x    xxxx        │                 x               │
   │                                       │    xxxxxxxx    xxxxxx           │                 x               │
   │                                       │                                 │                 x               │
   │                                       │                                 │                                 │
   │                                       │                                 │                                 │
   ├───────────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
   │                                       │K                                │L                                │
   │J                                      │                                 │                                 │
   │                                       │                                 │      xxx xx xx xx               │
   │                                       │            xxxxxx xxxxxx        │     xx          xx              │
   │               xxxxxx                  │          xx           xxxxxx    │     x            x              │
   │                x   x                  │         xx    xxxxxxxxxxxxxxx   │     x            x              │
   │               xx   x                  │         x   xx                  │     xx           x              │
   │            xxxxxxxxxxxxx              │         x   xx                  │      x           x              │
   │             xx       xxx              │         xx    xxx               │      x           x              │
   │              xx     xx                │          xx     xxxxxxxxxxxx    │      xxxxxxxxxxxxx              │
   │               xx   x                  │           xxxxxxxxxxxxxxxxxx    │                                 │
   │                xx x                   │                                 │                                 │
   │                 xx                    │                                 │                                 │
   │                                       │                                 │                                 │
   └───────────────────────────────────────┴─────────────────────────────────┴─────────────────────────────────┘
```
The chamber is divided into twelve blocks with red glowing symbols on them.
Every time a square. Every time a square is triggered, it's symbol flashes,
then stops glowing.

### A Smile
1d4 specters appear

### B Frown
A red crystal appears and the door opens.

### C Evil
DC 18 wisdom save, or the creature that touched the square is controlled and
hostile for 1d4 turns.

### D E!
The word "E!" is called out.
Resets all squares, which begin glowing again.

### E Fire
Fireball centered on the square

### F Triangle
A spectral forest giant and two spectral dire wolves will appear.

### G Circle
Moon beam blast. DC 14 CON save to halve 4d6 radiant

### H Three Face
Creature transforms into a random animal

```
+------+--------+
| Roll | Animal |
+------+--------+
|    1 | Cat    |
|    2 | Bunny  |
|    3 | Weasel |
|    4 | Frog   |
+------+--------+
```

### I Tree
A grass heap grows from the ground and fights.

### J Arrowhead
1d6 spectral archers appear

### K Crescent Moon
1d6 spectral wolves

### L Square
Four spectral swordsmen

## Room 5: Boss
```
  ┌────┬───┬────┬──────────────────────────────────────────────────┐
  │    │   │    │                                                  │
  │15ft│   │    │                                                  │
  ├────┘   │    │      ┌────┐                                      │
  │    10ft│    │      │ A  │                                      │
  ├────────┘    │      └────┘                                      │
  │     5ft     │                                                  │
  ├─────────────┘                                                  │
  │                                                                │
  │                                                                │
  │               ┌────────────────────────────┐                   │
  │               │                            │                   │
  │               │                   5ft      │                   │
  │               │                            │                   │
  │               │      ┌─────────────────────┤                   │
  │               │      │                     │                   │
  ├┬─────┐        │      │                     │         ┌────┐    │
  ││  A  │        │      │            10ft     │         │    │    │
  ││     │        │      │         ┌───────────┤         │ A  │    │
  ├┴─────┘        │      │         │           │         └────┘    │
  │               │      │         │  15ft     │                   │
  │               │      │         │           │                   │
  │               │      │         │           │                   │
  │               │      │         │           │                   │
  │               └──────┴─────────┴───────────┘                   │
  │                                                                │
  │                                                                │
  │                                           ┌────────────────────┤
  │                                           │                    │
  │                                           │                    │
  │     ┌────┐                                │                    │
  │     │ A  │                                │                    │
  │     └────┘                                │       -10ft        │
  │                                           │                    │
  │                                           │                    │
  │                                           │                    │
  └────────────────────────────x──────────────┴────────────────────┘
A: Fire pits
```
When the party enters, the fire pits light up blue, green, gold, and red.
That's when the specter of Doramir appears. He snaps his fingers and three
doubles appear. "You want my hammer? Prove yourselves!."

## Monster stat blocks
```
Specter
Medium Undead
HP: 21 (3d8+6)
Speed: 30ft
Resist: Non-magical physical, necrotic
Weak: Radiant
Life Drain +4 1d10 necrotic
Spectral Shortsword +4 1d6+2 slashing

Skeleton
Medium Undead
HP: 10(2d8)
AC: 13
Speed: 30
Weak: bludgeoning
Blindsight: 30ft
Shortsword +4 1d6+2 piercing
Shortbow +4 1d6+2 piercing

Bone Heap
Large Undead
HP: 44 (4d20)
AC: 12
Speed: 30ft
Weak: Bludgeoning
Reform: At the start of it's turn, the bone heap restores 1d6 hit points.
Engulf +4 1d4 bludgeoning. Target must succeed DC 14 STR save or be restrained.
Can remake save using their action.
Pummel: Restrained target must succeed DC 14 DEX save to halve 4d4 bludgeoning damage.

Breath Skull
A floating skull wreathed in brightly colored dragon's breath.
Tiny Undead
HP: 30 (5d6+6)
Speed: fly 15ft
Element: The dragon's breath is either fire, lightning, acid, or poison.
The breath skull is resistant to this type of damage, and it's breath attack
deals this damage type.
Dragon's Breath: 15ft cone DC 15 DEX save to halve 3d6(see element for type)

Bone Gauntlet
An armored skeleton wielding a morning star.
Medium Undead
HP: 27(3d8+12)
AC: 18(rusty plate mail)
Speed: 30ft
Morning Star(10ft) +4 1d8+4 bludgeoning

Skelemancer
A robed skeleton with a rusty, blood-crusted dagger
Medium Undead
HP: 24(3d8+9)
Speed: 30ft
Raise(Recharge 3-6): Every bone pile and corpse within 15ft are raised as a
skeleton or zombie, respectively. They each have 1d4 hit points.
Letter +4 1d4+2 piercing, 1d6 necrotic

Reaper
Medium Undead
HP: 18 (3d10)
AC: 13
Speed: Float 30ft
Weak: Bludgeoning
Scythe Block: As a reaction when targeted with a melee attack, add +2 to AC for
this attack by blocking with scythe. If this blocks the attack, the attacker
must succeed a DC 14 STR save or drop their weapon.
Scythe +6 2d6+2 magical slashing
Life Drain(10ft) +6 1d8+2 necrotic. Heals damage dealt.

Ghost
Medium Undead
HP: 50(10d8)
AC: 14
Speed: Fly 40ft
Immune: Non-magical physical, necrotic
Weak: Radiant
Incorporeal form: The ghost may become incorporeal and pass through objects.
They may not attack while incorporeal.
Life Drain: +4 1d10 necrotic

Spectral Forest Giant
These creatures live among moose, dire wolves, and bears. They reflexively
kill humanoids, thinking they are all hunters coming to kill their friends.
They have woody vines growing on them, along with mosses. This spectal giant
thinks it's in a forest.
Large Giant
HP: 40 (5d12+5)
AC: 15 (vine armor)
|STR|DEX|CON|INT|WIS|CHA|
| 18| 12| 14|  8| 16|  4|
Vulnerable: Fire
Immune: Poison
Healing sap: Every turn, the forest giant can gain 1d6 temporary HP
Vine strangle(15ft) +5 1d4 bludgeoning, creature is grappled pulled 15ft closer.
Poison oak great club +5 2d8 bludgeoning + 2d4 poison

Spectral Wolf
Medium beast
HP: 18 (3d8+3)
AC: 12
|STR|DEX|CON|INT|WIS|CHA|
| 14| 12| 12|  4| 12|  4|
Pack tactics: When attacking a target adjacent to a friendly, the wolf
gains advantage on the attack.
Bite +4 1d8+2
Claws +4 2d4+2 slashing

Spectral Dire Wolf
Large beast
HP: 29 (3d12+9)
AC: 12
|STR|DEX|CON|INT|WIS|CHA|
| 16| 12| 16|  4| 12|  4|
Pack tactics: When attacking a target adjacent to a friendly, the wolf
gains advantage on the attack.
Bite +4 2d8+3
Claws +4 2d6+3 slashing

Grass Heap
Huge Plant
HP: 87 (9d12+24)
AC: 12
Speed: 40ft
Resistances: non-magical physical damage, cold
Vulnerabilities: fire
Spore Cloud: 30 foot radius, DC 14 CON save or become poisoned
Tree club: +7 19(3d8+4) bludgeoning

Spectral Archer
Medium Undead
HP: 15(3d6+3)
AC: 15(Scale mail)
Speed: 30ft
|STR|DEX|CON|INT|WIS|CHA|
| 12| 16| 12| 12| 12| 12|
Multi-attack: Can make two attacks with longbow
Attacks:
Dagger +5 1d4+3 piercing
Longbow +5 1d8+3 piercing

Sprectral Swordsman
Medium Undead
HP: 21(3d8+6)
AC: 15(Scale mail)
Speed: 30ft
|STR|DEX|CON|INT|WIS|CHA|
| 14| 12| 14| 12| 12| 12|
Martial Advantage: When the target is within 5ft of an ally, melee attacks deal
an addition 1d8 damage.
Projectile deflect: With a reaction when attacked with a ranged weapon, swordsman
can add +2 AC for that attack to attempt to deflect the projectile.
Attacks:
Longsword +4 1d8+2

Doramir's Ghost
Medium Undead
HP: 70(10d12)
AC: 14
Speed: fly 30ft
Resist: Non-magical physical
Doubles: At the end of Doramir's turn, all of his doubles turn invisible for
a second and their position shuffles.
Firebolt +7 1d10 fire
Chain(15ft) +5 1d6 slashing. Pulls creature 15ft.

Doramir's Double
HP: 20
AC: 14
Speed: fly 30ft
Chain +5 1d6 slashing
Resist: Non-magical physical
Chain(15ft) +5 1d6 slashing. Pulls creature 15ft.
```