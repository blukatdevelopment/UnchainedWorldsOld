```
################################################################################
# ______     _           _                                                     #
# | ___ \   (_)         | |                                                    #
# | |_/ / __ _  ___  ___| |_                                                   #
# |  __/ '__| |/ _ \/ __| __|                                                  #
# | |  | |  | |  __/\__ \ |_                                                   #
# \_|  |_|  |_|\___||___/\__|                                                  #
# V0.0.0                                                                       #
################################################################################
```
You live as an example to all that share your faith. In service of a deity,
you live by a strict code of conduct and leverage your piety to wield your
deity's magic.

## Skills
Choose two from the following:
- Religion
- Persuasion
- Medicine
- Insight
- History
- Perception

## Starting equipment
- Dagger or mace
- Holy Book
- Holy Symbol

```
+-------+--------------------+----------+-------------+------------------------+
| Level | Minimum Experience | Hit Dice | Spell Level |        Features        |
+-------+--------------------+----------+-------------+------------------------+
|     1 |                  0 | 1d4      |   Cantrip   | Divine Spellcasting    |
|     2 |                300 | 1d4      | 1           | Domain                 |
|     3 |                900 | 1d4      | 2           |                        |
|     4 |               1200 | 2d4      | 2           |                        |
|     5 |               2700 | 2d4      | 3           | Ability Score Increase |
|     6 |               5000 | 2d4      | 3           | Channel Divinity       |
|     7 |               7500 | 3d4      | 4           |                        |
|     8 |              10000 | 3d4      | 4           |                        |
|     9 |              15000 | 3d4      | 5           |                        |
|    10 |              20000 | 4d4      | 5           | Ability Score Increase |
+-------+--------------------+----------+-------------+------------------------+
```

## Feats

### Divine Spellcasting
You've learned to call upon the power of a deity. Wisdom is your spellcasting
ability. You learn two cantrips

```
+-------------+-------------+
| Spell Level |  Piety Cost |
+-------------+-------------+
| Cantrip     |          25 |
| 1           |         200 |
| 2           |         800 |
| 3           |        2400 |
| 4           |        7200 |
| 5           |       21600 |
+-------------+-------------+
```

#### Preparing Spells
Before you sleep at night, you may perform a prayer to request a number of
spells equal to your wisdom modifier. You may select these spells from the 
priest spell list, and they must be first level or higher. You may only cast
spells that you have prepared.

#### Piety
A deity provides your source of magic, and so your fuel for spellcasting
is piety. Your actions are judged, providing and revoking piety. If your
balance of piety ever reaches or falls below zero, you lose all all divine
spellcasting and magical abilities.

```
+-----------------------------------+--------------+
|            Good Acts              | Piety Gained |
+-----------------------------------+--------------+
| Lead Prayer(Short Rest)           | 1d100        |
| Provide counsel(Roleplay it)      | 2d100        |
| Honorable Act(Domain Specific)    | 1d2 * 100    |
| Alms to the poor                  | 5d100        |
| Convert believer                  | 1d10 * 100   |
| Apprehend Criminal                | 1d10 * 100   |
| Sacrifice heart of large monster  | 1d4 * 1000   |
| Save a life from immediate danger | 1d12 * 100   |
| Cure the sick                     | 1d2 * 1000   |
| Sacrifice heart of huge monster   | 1d6 * 1000   |
+-----------------------------------+--------------+
```

```
+-------------------------------+-------------+
|          Bad Acts             | Piety Lost  |
+-------------------------------+-------------+
| Blasphemy or profanity        | 1d10 * 1000 |
| Murder                        | 2d20 * 1000 |
| Forbidden Act(Domain specific)|  1d6 * 1000 |
| Deceive, Cheat, or Steal      | 1d20 * 100  |
+-------------------------------+-------------+
```

### Domain
You have earned enough trust from you deity to access their special reserve of
spells. With this trust, you will be responsible for abstaining from forbidden
acts. Domain spells do not count against the number of spells you may prepare.


```
+-----------+-----------------------+------------------------+----------------------------------------+
|  Domain   |     Honorable Act     |     Forbidden Act      |                Spells                  |
+-----------+-----------------------+------------------------+----------------------------------------+
| Light     | Lighting a new shrine | Leaving a shrine unlit | Light[1], Dazzling Light, Bend Light   |
| Life      | Blessing an newborn   | Killing a humanoid     | Spare the dying[1], Mana, Revivify     |
| Nature    | Planting a tree       | Cutting a tree         | Thornwhip[1], Vine Suit, lightning bolt|
| Knowledge | Teaching someone      | Keeping a secret       | Eye stone[1], Identify, Mind Probe[1]  |
|           | for an hour           |                        |                                        |
| Justice   | Provide Judgement     | Fail to fight bad acts | Chastise, Smite, confess               |
|           | for a crime           | of others              |                                        |
+-----------+-----------------------+------------------------+----------------------------------------+
[1]: Spell is found in the Spell Compendium Volume 1
```

### Channel Divinity
As the discipline in your domain grows solid, your deity offers up a domain-specific ability.
After you use this ability, you must complete a partial or full rest before you can use it
again. Channeling divinity takes an action.

#### Holy Light (Light Domain)
You outstretch your arms and a 60 foot diameter cylinder that extends from the 
sky to your feet illuminates it's space as if in bright daylight. The light
crosses through solid objects and may penetrate into subterranean spaces.
Creatures cannot hide within the light, and invisible creatures become
visible. Any friendly creatures within the light are immune to necrotic damage
and any enemy creatures within the light are vulnerable to radiant damage.
The light lasts for 1 minute.

#### Miasma of Restoration (Life Domain)
You call out the name of your deity and smoke rolls out of your nostrils, ears,
and mouth. A 15 foot radius cloud forms around you and heavily obscures visibility.
Any creature which begins it's turn within or enters the cloud is healed for 1d6
hit points. You may use an action each turn to sustain the cloud. The effect
lasts up to 1 minute.

#### Spirit Bomb (Nature Domain)
You hold your hands with wrists touching and call out to the spirits of nature
to lend you their energy. An orb of spirit energy forms in front of your
hands as you siphon the collective energy of the plants and animals on your
plane of existence. Now, and until this effect ends, you may choose to
build or release the channeled energy.

You may release the spirit bomb by firing it at a point within 120 feet, The orb
explodes on impact and all creatures within a 30ft range must make a dexterity
saving throw, taking 2d8 radiant damage on a failure and half as much on a
success. Within the point of impact any metal objects degrade into piles of rust
powder. This ends the channel divinity.

You may build the channeled energy further, growing the orb. The radius when you
release the spirit bomb increases by 5ft, and the damage dealt increases by 2d8,
up to a maximum of 50ft and 10d8 radiant damage. You must hold concentration to
build the spirit bomb's energy.

#### Omniscient Sight (Knowledge Domain)
Your eyes begin to glow brightly. You can see all creatures within 120 feet of
you, whether they are invisible, hiding, or in a parallel dimension such as the
ethereal plane. You chant a holy prayer, and any friendly creatures within
range share this sight, and additionally gain advantage on any attack rolls
they make. Each turn, you may use your action to continue chanting in order to
extend this effect for up to 1 minute.

#### Reap (Justice)
You use one hand to point at an evil creature within 60 feet, and hold your
other hand in the air as you declare that the creature will be reaped in the
name of your deity. A spectral scythe appears in your hand. You are proficient
with the scythe and it uses wisdom instead of strength. The scythe deals 3d10
force damage on a hit. If you kill the targeted creature, their soul is harvested
and you receive 1d2 * 1000 piety. The weapon disappears after 1 minute, or if
you end a turn without having attacked with it, or after killing the targeted
creature.

## Spell List

### Cantrip
- Mending[1]
- Sacred Flame
- Guidance
### 1st
- Guiding Bolt
- Healing Word
- Cure Wounds
- Shield of Faith
- Calm Emotions
- Command
- Protection from good and evil[1]
### 2nd
- Insight Arrow
- Radiant Weapon
- Holy Weapon
- Bird Friend
### 3rd
- Sacrifice
- Kindness
- Confession
- Riddle[1]
### 4th
- Miracle
### 5th
- Judgement
- Curse[1]
- Angelic Transformation
[1] - spell is found in the Spell Compendium Volume 1

## Spells

```
Guidance (Cantrip)
Casting time: 1 action
Range: 30 feet
Components: V
Duration: 1
You call out a phrase of caution, encouragement, or comfort to one target that
can hear and understand you within range. Within the duration, they may add 
1d4 to one ability check, skill check, or saving throw, ending the spell.
```

```
Sacred Flame (Cantrip)
Casting time: 1 action
Range: 60 feet
Components: V, S
Duration: Instantenous
A radiant flame appears on a target within range that you can see. They must
succeed on a dexterity saving throw or take 1d6 radiant damage.
```

```
Dazzling Light (1st)
Casting time: 1 reaction, when a creature attempts to attack you from within 5ft
Range: 5ft
Components: S
Duration: Instantaneous
You raise your hand and bright light flashes at the creature, partially blinding
it. The creature must make a wisdom saving throw. On a success, they have
disadvantage on their attack. On a failure, they cover their eyes, ending it's
turn.
```

```
Smite (1st)
Casting time: 1 action
Range: self
Components: s
Duration: Instantaneous
You make an unarmed or weapon melee attack as part of this action, and your
weapon or fist glows with radiant fire when you do. If the attack hits, this
attack deals an additional 3d8 radiant damage.
At higher levels: When cast above level 1, the smite deals an addition 1d8
radiant damage per level above first.
```

```
Mana (1st)
Casting time: 1 minute
Range: Touch
Components: V, S, M (a pile of up to 20 rocks)
Duration: Instantaneous
You convert a pile of up to 20 rocks into mana. This fluffy, sweet-tasting pink
bread has a delicate crust and will last for one week. Each loaf of mana counts
as one pound of food.

```

```
Vine Suit (1st)
Casting time:
Range: Self
Components: V, S, M(nearby plants)
Duration: 1 hour
You coax nearby plants to sprout into vines that cover your form. This grants
you 1d4+2 temporary hit points and confers advantage on stealth checks made in
foiliage for the duration. This spell ends if you lose your temporary hit points.
```

```
Identify (1st)
Casting time: 1 action
Range: Touch
Components: V, S, M (a pearl or monocle worth 10GP)
Duration: Instantaneous
You hold one object in your hand and immediately learn if it is a magical item,
and what magic it contains. Curses are not revealed by this spell.
```

```
Healing Word (1st)
Casting time: 1 Bonus action
Range: 60 feet
Components: V
Duration: Instantaneous
You speak a holy word or phrase to one creature who can hear you within range.
They gain hit points equal to 1d6 plus your spellcasting modifier.
```

```
Cure Wounds (1st)
Casting time: 1 action
Range: Touch
Components: S
Duration: Instantaneous
You touch one creature and grant them healing energy. They restore hit points
equal to 1d10 plus your spellcasting modifier.
```

```
Shield of Faith (1st)
Casting time: 1 action
Range: self
Components: V, S 
Duration: Concentration, 1 minute
You hold out a spare hand and a glowing spectral shield appears in it. This
shield increases your AC by +2.
```

```
Calm Emotions (1st)
Casting time: 1 action
Range: 30 feet
Components: V
Duration: Concentration, up to 1 hour
You speak a calming phrase, quote a holy book, or sing a relaxing song to a creature which is intensely emotional and can understand you.
The creature must succeed a wisdom saving throw, or feel calm. When the spell ends, the creature learns that you have used magic to manipulate them, but must
succeed an intelligence saving throw to feel anything but neutral about it.
```

```
Command (1st)
Casting time: 1 action
Range: 60 feet
Components: V
Duration: Instantaneous
You speak a command word to one creature within range that can hear you. The
creature must succeed a wisdom saving throw to avoid following the command.
The commands include:
- Drop: The creature falls prone where they stand, dropping any items they are carrying.
- Run: The creature moves in the opposite direction of you their entire movement.
- Silence: The creature cannot speak or produce audible sounds for 1 minute. They may repeat their save to end this effect.
- Sing: The creature belts out a song for 1 minute. They may repeat their save to end this effect.
```

```
Radiant Weapon (2nd)
Casting time: 1 action
Range: touch
Components: V, S, M (One-handed melee weapon you are proficient with)
Duration: Concentration, 1 minute
You speak a command word and the weapon in your hand burns with a radiant flame.
For the duration, your attacks with this weapon deal an additional 1d8 radiant
damage.
At higher levels: When you cast this spell at a 3rd or higher level,
the damage increases by 1d8 for each level.
```

```
Holy Weapon (2nd)
Casting time: 1 bonus action
Range: 60 feet
Components: V, S
Duration: Concentration, 1 minute
You conjure a spectral weapon of your deity which floats in the air in a point
within range, and it attacks a creature. Make a melee spell attack. On a hit,
the weapon deals 1d6 force damage.
At higher levels: When cast at a 3rd or higher level, the damage increases by
1d6 for each level.
```

```
Bird Friend(2nd)
Casting time: 1 action
Range: 1 mile
Components: V, S, M (a feather)
Duration: 8 hours
A bird appears from thin air, imbued with a friendly celestial spirit. You may whisper to it a destination within range,
and it will attempt to fly to this location, survey it, and return to tell you the lay of the land. The bird has an AC
of 16 and 1 hit point. It disappears once it tells you about what it saw or the duration ends.
```

```
Confession (3rd)
Casting time: 1 action
Range: 30 feet
Components: V, S, M
Duration: Concentration, up to 1 minute
You speak a command word to a creature, and it must succeed a wisdom saving
throw or begin making confessions for the duration. The creature must only
state confessions that they feel genuine guilt about.
```

```
Sacrifice (3rd)
Casting time: 10 minutes
Range: Self
Components: V, S, M(an object, which is consumed by the spell)
Duration: Instantaneous
You destroy an object of great value and please your deity, gaining peity.
The amount of peity depends on the object.
+------------------------+-------------+
|       Sacrifice        |    Piety    |
+------------------------+-------------+
| 100gp worth of objects | 2d8 * 1000  |
| +1 weapon              | 3d10 * 1000 |
| A murderer's heart     | 2d20 * 1000 |
| +2 weapon              | 3d20 * 1000 |
+------------------------+-------------+
```

```
Lightning Bolt (3rd)
Casting time: 1 action
Range: 100 feet
Components: V, S, M (a piece of glass formed by a lightning strike)
Duration:
You hold out your hand and a bolt of lightning leaps from it in a straight line
for 100 feet. Every creature in the bolt's path must make a dexterity saving
throw. On a failure they receive 6d6 lighting damage, and half on a save.
```

```
Bend Light (3rd)
Casting time: 1 action
Range: 120 feet
Components: V, S, M (A prism)
Duration: Concentration, 1 minutes
You create a 15 foot radius sphere of influence on a point centered within
range, and can produce an effect on that space. You may use your action to move
the space up to 30 feet and change the effect or target. Such effects include:
- Darkness: No light can pass through the space, and it is filled with darkness.
- Mirage: The sphere shows what is on the opposite side, rendering everything inside seemingly invisible from a distance.
- Beam(requires direct sunlight): You direct light at one creature within 60 feet of the sphere. It must make a con save, receiving 4d6 radiant damage on a failure and half as much on a success.
- Spotlight: You form the light into a narrow cone and aim it at a target within 60 feet, illuminating it selectively.
- Intensify: Any light-sources within the sphere of influence double the range of their light
- Blind(Requires bright light): You target one creature in range, bending all light into it's eyes. It is temporarily blind.
```

```
Kindness (3rd)
Casting time: 1 action
Range: 60 feet
Components: V
Duration: Concentration, up to 10 minutes
You speak a compliment to a creature that can understand you. The creature must
succeed a wisdom saving throw, or else become charmed with a powerful sense of
affection for every creature it encounters, treating them as a beloved family
member or close friend. When the spell ends, the creature is fully aware that
you have manipulated it with magic.
```

```
Revivify (4th)
Casting time: 1 action
Range: Touch
Components: V, S, M (A gem worth 100GP, which is consumed)
Duration:
You speak a command word while holding a gem, and it shatters into a cloud of
mist. You then touch one creature that has died in the last ten minutes, and the
mist enters their nostrils or otherwise seeps into them. Roll a 1d20. On a 1,
this spell fails.
```

```
Miracle (4th)
Casting time: 1 action
Range: 120 feet
Components: 
Duration: Instantaneous
You pray to your deity for some form of divine intervention in a moment of great need.
Roll 1d4. On an odd result, roll another to figure out which of the following happens:
1d4
1: Any water within range turns to wine.
2: Any loaves of bread or fish within range multiply by ten times.
3: Any quarterstalves in range turn into poisonous snakes.
4: One random dead creature within the spell's range is resurrected.
On an even result, the following happens:
The deity causes some event to happen around you, as specified by the GM. This
event helps the caster in some tangible way if possible, and must be an event which could
be explained as merely a very unlikely coincidence by someone skeptical of said
deity's influence.
```

```
Judgement (5th)
Casting time: 1 action
Range: 120 feet
Components: V, S
Duration: Concentration, up to 1 minute
Your eyes glow with holy fire and if you have hair, it turns golden for the
duration. For the duration, you may use your bonus action to name one sin
committed by a creature within range. That creature must make a wisdom saving
throw. On a failure, they receive the damage listed in the chart below, or
half as much on a success. You must have witnessed them perform the sin you
are judging them for. Each creature can be judged for each sin only once.
+-------------------------------+----------------+
|          Sins                 | Radiant Damage |
+-------------------------------+----------------+
| Blasphemy or profanity        | 2d8            |
| Murder                        | 10d8           |
| Forbidden Act(Deity specific) | 3d8            |
| Deceive, Cheat, or Steal      | 1d8            |
+-------------------------------+----------------+
```

```
Angelic Transformation (5th)
Casting time: 1 bonus action
Range: self
Components: V, S
Duration: Concentration, up to 10 minutes
Your body is bathed in holy light, and you transform. You may select three listed
features for your transformation, which end after the duration.
- Wings: You gain a flying speed of 60 feet
- Extra arms: You gain one extra attack per attack action that uses these arms.
- Extra legs: You gain a climbing speed of 40ft, and your unrmed attacks deal 2d6 bludgeoning damage.
- Staff of light: A staff made of pure burning radiant energy appears in your hands, and you are proficient with it. It deals 2d10 radiant damage.
- Rain bow: A bow appears in your hands made of multicolored light. It deals 2d10 radiant damage on a hit.
- Holy armor: Your body is encased in glowing plate mail. Your AC is now 18, and you may still use a shield.
- Size: You grow two sizes larger. You gain 3d10 temporary hit points.
- Eyes: Glowing symbols of eyes float around you. Weapon attacks have disadvantage on you, and you have advantage on dexterity saving throws.
```