# Monster Guide

## How to make a monster
### Minimal stat block
Minimum, you'll need HP, AC, and one attack. When ability checks are made, you can either assume a +0, or some other modifier on the fly.
`Dogron, HP: 6, AC: 12, Bite +5 D6`

### Extra stats: Ability scores
Adding an array of ability scores if the bonuses on checks and saves are particularly important for this monster. (ex: `[15, 13, 8, 20, 12, 15]`) This'll help solidify modifiers for melee and ranged weapons as well as spellcasting, if it applies. Alternatively, you could just put a single modifier `[All +1]` if you want to go half-way on ability scores.

### Extra stats: Passive abilities
If you want to reduce rolls for your monsters, you can jot down one or more passive scores. The passive version of an ability is 10 + mod, and add half the size of any skill dice it might have. You can use these passive abilities in place of making rolls. This is especially helpeful when determining if a large group of monsters detects a sneaking PC.

### Extra: Spellcasting
Use the instructions on creating spells in the keepers guide, then apply them. Default to pact and especially naming magic if possible, so as to keep the spells in use flexible.

### Extra stats: Special powers
A special power is some unique mechanic that makes fighting the monster fresh. Popular options:
- Limit PC mobility or move them around
- Gain extra mobility(teleport, fly, burrow, climb, phase through walls)
- Alter visibility(invisibility, cammoflauge, smoke cloud)
- Inflict a bespoke condition(poison, disease, hallucinations, parasites, fear, mutation)

### Extra stats: Multiple States
If you are making a particularly tough enemy with many HP, you may wish you give it multiple stat blocks each with their own chunk of HP. When the first runs out of HP, don't carry over overkill damage. Give each stat block a different set of special powers, and maybe a different style of behavior(such as panic, getting serious, fleeing)

### Extra stats: Variable actions
If you want to nerf monsters that are intended to appear in large amounts, give them less actions. Likewise, you may increase a monster's power by giving it more. Note that there is no fourth attack option.

## Archetypal stat blocks
Change out the name and slap some powers on. Boom! You've got a monster. You may wish to swap the abilities from a single modifier to scores, change attacks, etc, but that's up to you.

### Vermin
```
Vermin, HP: 1(D2), AC: 8, [All -1]
Bite +1 1
```

### Mook
```
Mook, HP: 9(D6+6), AC: 10, [All +0]
Club +2 D4
```

### Elite Mook
```
Elite Mook, HP: 18(2d6+12), AC: 11, [All +1]
Sword +3 D6
```

### Tank
```
Tank, HP: 27(3d6+18), AC: 12, [All +2]
Attack +4 D12
```

### Mini-Boss
```
Mini-Boss, HP: 54(6d6+36), AC: 13, [All +5]
Bite +5 D12
```

### Boss
```
Boss, HP: 108(12d6+72), AC: 15, [All +6]
Bite +6 D12
```

## Bandits
```
Bandit, HP: 10, AC: 13(leather) [14, 14, 10, 10, 10, 10]
Unarmed +2 D2
Rusty Sword +2 D6
Shabby Bow +2 D6
Loot: 3d4 SP
```

```
Bandit Captain, HP: 15, AC: 11(leather) [16, 10, 15, 10, 12, 13]
Unarmed +5 D2
Dual Rusty Scimitars +5 2d6kh1
Crossbow +2 D8: 2 actions to reload
Loot: 3d4 GP
```
### Lore
Bandits live on the outskirts of civilization, using the monster-ridden wilds and ruins therein to protect against scouts and search parties. Bandits attack travelers, generally charging little or nothing from the peasantry. Bandit hideouts often serve as a hub for black market commerce and a safe haven for criminals and persecuted individuals alike.

### Variations
Roll for a type of bandit group. You may roll multiple and decide whether they ignore one another, compete for a market or resource, or otherwise cooperate.
1. Street Gang
2. Crime Haven
3. Suppliers
4. Highwaymen
5. Warlord
6. Rebels

#### Street Gang
Street gangs oversee racketeering, robberies, dealing black market items. With active resistance from the law, they are likely to rely on easily concealed or improvized weapons such as daggers, clubs, and hand crossbows, and are less likely to wear armor or uniforms. Street gangs who have competition tend to wear common colors to 
Roll 3d6 for table below to create a street gang.

| D6 | Racket     | Black Market | Defense         |
|:---|:-----------|:-------------|:----------------|
|  1 | Salt       | Moon Dust    | Powerful leader |
|  2 | Water      | Moon Grass   | Thug army       |
|  3 | Meat       | Weapons      | Special weapons |
|  4 | Metal      | Magic        | Bribery         |
|  5 | Protection | Assassins    | Terror          |
|  6 | Laundering | Fences       | Infiltration    |

#### Crime Haven
Den of smugglers, crime bosses, asylum-seekers, and opportunists. Havens generally act to connect one or more other groups of bandits. Bandits in crime havens are extremely likely to employ ostentatious and illegal weapons or armor in plain sight without fear of legal recourse. Those not affiliated with the owner are sometimes disarmed at the door when doing business to prevent bloodshed over disagreements.
Roll 3d6 for table below to create a crime haven.

| D6 | Owner              | Workers            | Building
|:---|:-------------------|:-------------------|:---------------|
|  1 | Crime boss         | Thugs              | Keep           |
|  2 | Corrupt Merchant   | Street urchins     | Walled village |
|  3 | Cult leader        | Religious refugees | Temple         |
|  4 | Mercenaries        | Escaped convicts   | Camp           |
|  5 | Monster            | Adventurers        | Cave network   |
|  6 | Bounty Hunters     | Corrupted          | Island         |

#### Suppliers
Suppliers grow, manufacture, or collect black market goods.
Roll 3d6 for table below to create a group of suppliers.

| D6 | Good           | Defense     | Workers   |
|:---|:---------------|:------------|:----------|
|  1 | Moon Dust      | Monsters    | Peasants  |
|  2 | Moon Grass     | Traps       | Thugs     |
|  3 | Weapons        | Remote      | Monsters  |
|  4 | Organs         | Cultists    | Corrupted |
|  5 | Counterfeits   | Disguise    | Cultists  |
|  6 | Mercenaries    | Mercenaries | Orphans   |

#### Highwaymen
Highwaymen rob caravans, impose fees and tolls on travelers. More often than not, these groups are criminal in nature, but occassionally they may get permission from a kingdom by offering a cut of their earnings. Sometimes these groups are sent directly by kingdoms.
Roll 3d4 for table below to create a group of highwaymen.

| D6 | Leader     | Workers        | Strength  |
|:---|:-----------|:---------------|:----------|
|  1 | Monster    | Corrupt guards | Numbers   |
|  2 | General    | Veterans       | Training  |
|  3 | Peasant    | Peasants       | Magic     |
|  4 | Crime boss | Corrupted      | Gear      |

#### Warlord
Warlords raise an army to collect taxes and tribute as well as to pillage. Warlords can have ambitions of rivaling nearby kingdoms or merely sustaining a life of luxury and power for the leader. Roll 2d4 for the table below.

| D4 | Leader              | Army              |
|:---|:--------------------|:------------------|
|  1 | Monster             | Monsters          |
|  2 | Defected General    | Defected soldiers |
|  3 | Crime Boss          | Thugs             |
|  4 | Merchant            | Mercenaries       |

#### Rebels
Rebel groups generally organize to resist the current rulers for a cause that is deemed just. Charismatic leaders centralize the power of such efforts, making it easier to disband or pacify their groups through coercion, bribery, or elimination of said leader. Groups with unremarkable or anonymous leaders are far more difficult to dissuade.
Roll 2d6 for the columns of the table below.

| D6 | Leader           | Agenda        |
|:---|:-----------------|:--------------|
|  1 | Religious Figure | Meet demands  |
|  2 | Commoner         | Depose rulers |
|  3 | Idealogue        | Revolution    |
|  4 | General          | Become Leader |
|  5 | Anonymous Figure | Revenge       |
|  6 | Merchant         | Corner Market |

## Authorities
Stable humanoid settlements gather around some set of norms. When you violate these norms sufficiently, or attempt to change them, you learn who holds authority.

Roll once to make a simple settlement, twice to make one with tension and conflict, and three or more times to create an environment conducive to political intrigue.
1. Royals
2. Nobles
3. Commoners
4. Merchants
5. Sages
6. Reroll

### Royals
Royals are a miniscule minority which are famously offered few checks or balances. The difference between royals and warlords is primarily in technique. While a warlord must fight an ongoing war with their tributaries to keep them beaten into submission, royals rely on a myth to do that for them. For a simpler group of royals, roll a D3 (or D4, discounting 4s) for their myth, or roll twice(rerolling on a duplicate) for royals with a main and secondary myth.

1. Birthright
2. Popularity
3. Terror

#### Birthright
A royal bloodline is the legacy of more aggressive power brokers. The most mundane birthright is reinforced by other authorities for its own sake. More exotic birthright might be tied to an ancestry including eldritch, fey, dragon, or demon blood in addition to humanoid. Lastly, divine birthright may come from a powerful supernatural entity's favor of the royals, or at least of the myth of such favor.

#### Popularity
Royals sell themselves, or the process that grants them power, as benevolent. A people's king may give gifts or share the spoils of war with the peasantry. An election may take place between multiple royals, all sharing similar vested interest in preserving the same status quo.

#### Terror
Royals instill fear in their subjects, either of the royals themselves, or some real or imaginary enemy. When the people believe their survival depends upon the royals, they are more likely to cooperate and compromise on their ideals. When the royals become the subject of fear, they aim for creating an image of resistance being hopeless and futile. The exchange of information is generally tightly controlled, and there is an ongoing task of finding and crushing cells of resistance.

### Nobles
Nobles are often granted a lesser power by Commoners or Royals only to later overpower them. You may roll for one type of noble.

1. Merchants
2. Mages
3. Diviners
4. Philosophers

#### Merchants
The wealth of successful merchants allows them to seize the most lucrative business opportunities, compounding their wealth over time as they minimize competition and maximize profit. The conversion of wealth into power through bribery is what allows merchants to gain power without getting their hands dirty.

#### Warriors
Nations with warrior cultures tend to find service fashionable, making it a precondition for noble status. In such socieities, upward social mobility is granted to warriors that fight particularly well. Left unchecked, the military may overtake a nation through a coups. The anxiety of a coups acts both as a check against military expansion and also as leverage in negotiating with competing agents.

#### Mages
The most common classes of mages are students of arcane magic

#### Diviners

#### Philosophers

### Commoners

## Cults
```
Cultist, HP: 10, AC: 12 [12, 14, 10, 16, 16, 16]
Dagger +4 D4
Naming magic: +6 DC 14
Pact Magic: +6 DC 14
Face Melt(DC: 8): one target, CON save or 3d6 damage
Dark sphere(DC: 10): 30ft sphere of magiclal darkness, lasts 1 hour
False Life(DC: 12): Gain 4d10 temporary HP
```

```
Fanatic Knight, HP: 16, AC: 15 [16, 12, 16, 12, 16, 12]
Greatsword +6 D12
Pact Magic: +6 DC 14
Flame Blade(DC 10): Blade attacks deal extra D6 damage for 1 minute
Dark sight(DC 10): Can see in even magical darkness for 1 minute
Faith Aura(DC12): Friendly creatures within 10ft receive +1 to AC for 1 minute
```

### Lore
A cult is measured not by miniscule size or obscurity of rhetoric, but of its capacity to focus power. A cult is nothing without charismatic leaders and fanatics willing to do whatever they say. Dogma and a keen focus on loyalty and devotion over all else make for a prime environment for the cult. Weaker cults may be relegated to living in tents surrounding a shrine, while larger ones may have their own orders of knights and even kingdoms. Fresh converts are typically selected by emotional vulnerability, using manipulative tactics such as lovebombing to earn enough trust to sever their outside connections and make leaving difficult.

Though cults may form around the personality of a single charismatic leader, they often have some magical power. Either the cult's leadership practices magic, or has artifacts that offer magical abilities, or has a pact with a creature such as a demon, devil, or undead that offers pact magic. No matter the magic involved, a cult will recruit will restrict magic to those who are most trusted by leadership.


### Variations

#### Demonic

#### Infernal

#### Undead

#### Outsider

#### Arcane

#### Namers

#### Mundane

#### Fey

#### Monster



#### Bandits

```
Bandit, HP: 10, AC: 13(leather) [14, 14, 10, 10, 10, 10]
Unarmed +2 D2
Rusty Sword +2 D6
Shabby Bow +2 D6
Loot: 3d4 SP
```

```
Bandit Captain, HP: 15, AC: 11(leather) [16, 10, 15, 10, 12, 13]
Unarmed +5 D2
Rusty Scimitar +5 D6
Crossbow +2 D8: 2 actions to reload
Loot: 3d4 GP
```

#### Cultist
You'll want to reflavor the spells based on who or what they worship.

```
Cultist, HP: 10, AC: 11 [8, 12, 10, 12, 14, 12]
Unarmed -1 D2
Dagger +1 D4
Divine Magic: +4 DC 12
- Face Melt: CON save or D12 damage
- False Life: Max HP increases by 10
Loot:
- D6 chance of random spell scroll
```

```
Cult Leader, HP: 10, AC: 11 [8, 12, 10, 16, 16, 16]
Unarmed -1 D2
Dagger +1 D4
Divine Magic: +4 DC 12
- Shadow form: Become shadow until next turn.
- Vitality drain: CON save or steal 4 STR and CON from target until dead or dismissed 
- Shadow swarm: 10ft radius, DEX save to halve 3d6 damage
Arcane Magic: +4 DC 12 
- Black tentacles: A portal opens and tentacles reach out to a target, who must succeed a STR save or take 1d6 damage as they are grappled.
- Death guard: Touch one creature and if they die in the next minute, they wake the next round with full HP.
- Shield: Cast automatically when you're attacked, raising your AC increases by 5 until your next turn starts.

Loot:
- Random magic item
- Spellbook with Black Tentacles, Death Guard, Shield
```

#### Soldiers

```
Archer, HP: 10, AC: 14(leather) [10, 18, 10, 10, 10, 10]
Unarmed +1 D2
Dagger +4 D2
Bow +8 D6
Loot: 2d4 SP
```

```
Spearman, HP: 15, AC: 13(leather+shield) [16, 10, 15, 10, 10, 10]
Unarmed +2 D2
Spear +5 D4
Loot: 3d4 SP
```

```
Knight, HP: 10, AC: 16(Plate) [18, 16, 20, 10, 12, 14]
Unarmed +4 D2
Greatsword +8 D12: May reroll once
Crossbow +3 D8: 2 actions to reload
Loot: 4d10 GP
```

## Generic monsters
These monsters have no brand identity. Don't be silly!

### Space Squid
Outsiders that dwell in deep bodies of water, featuring psionic powers and powerful intellects. Many rows of teeth. Evil and methodical.
```
Space Squid, Large, HP: 108(12d6+72), AC: 15, [All +6]
Tentacle +6 D12
Powers:
- Dominate(3/Day): DC14 WIS or mind controlled. Target repeats save when taking damage.
- Drain(2 actions): steal 2d4 HP from dominated creature
- Desire-vision: Probes minds for greatest desires.
- Mucous: Underwater within 5ft, DC15 CON or sick for D4 hours(can only breathe underwater)

```

### Angel Messenger
```
Angel Messenger, HP: 18(2d6+12), AC: 11, [All +1]
Holy Sword +3 2d6
Powers:
- Fly 30ft
- Half physical damage
Naming Magic: +4, DC14
- Shape
- Heal
```

### Angel Warrior
```
Angel Warrior, HP: 27(3d6+18), AC: 12, [All +2]
Holy Greatsword +4 D12
Powers:
- Fly 30ft
- Half Physical Damage
Naming Magic: +5, DC15
- Commune
- Plague
- Strike
- Raise
```

### Light Angel
```
Light Angel, HP: 54(6d6+36), AC: 13, [All +5]
Bite +5 D12
Powers:
- Fly 30ft
- Half Physical Damage
Naming Magic: +6, DC16
- Control
- Detect
- Resurrect
- Blind
```

### Spitting Antlion
```
Spitting Antlion, HP: 27(3d6+18), AC: 12, [All +2]
Bite +4 D12
Powers:
- Burrow 30ft
- Acid Spray(Recharge D6)(3 actions): Spits 30ft line of acid. DC 13 DEX save to halve 3d6 damage
```

### Basilisk
```
Basilisk, HP: 27(3d6+18), AC: 12, [All +2]
Bite +4 D12
Powers:
- See in dark
- Petrify: 5ft, DC 12 DEX or petrified
```

### Centipede Lizard
```
Centipede Lizard, Large, HP: 54(6d6+36), AC: 13, [All +5]
Bite +5 D12
Powers:
- Constrict: +5 D6, auto-grapple DC 15 STR
- Lightning Breath(Recharge D3)(3 actions): 20ft line, DC 16 DEX save to halve 4d6 damage
- Swallow: Grappled creature takes 2d6 acid damage per turn
```

### Tenticular Eyeballer
A floating ball with one eye and a gaping maw. Ten stalks with additional eyes.
```
Tenticular Eyeballer, Large, HP: 54(6d6+36), AC: 13, [All +5]
Bite +5 D12
Powers:
- Anti-magic Cone: 150ft cone of anti-magic from center eye
- Eye Rays: Roll below. DC 16 DEX save to dodge
1. Charm: Considers eyeballer a friend until attacked
2. Paralyze
3. Fear: -3 penalty to attacks
4. Slowing: -1 action for one hour
5. Enervation: DC16 CON to halve 4d8 DMG
6. Telekinetic: push 30ft
7. Sleep
8. Petrification 
9. Disintegration: 5d8 DMG
10. Death: 5d10 DMG
```

### Armored Tunneler
```
Armored Tunneler, Large, HP: 54(6d6+36), AC: 13, [All +5]
Bite +5 D12
Powers:
- Burrow 30ft
- Leap(3 actions): Jump 30ft, land on creatures. DC 16 DEX or 3d6 DMG
```

### Rotpede
An enormous centipede that feeds on dead things
```
Vermin, Large, HP: 54(6d6+36), AC: 13, [All +5]
Bite +5 D12
Powers:
- Climb 30ft
- Tentacles: 10ft +5 D4; DC 13 CON paralyze
```

### Chimera
A creature with dragon, goat, and lion heads. Front half lion, back half goat, and has dragon wings and tail.
```
Chimera, Large, HP: 54(6d6+36), AC: 13, [All +5]
Bite/Horns/Claws +5 D12
Powers:
- Fly 30ft
- Fire Breath(Recharge D3): 15ft cone DC15 DEX save to halve 4d8 DMG 
```

### Crabtaur
A crab beast with four legs and two arms ending in pinchers. Tentacles writhe from its face.
```
Crabtaur, Large, HP: 54(6d6+36), AC: 13, [All +5]
Pincer +5 D12, grapple on hit
Powers:
- Sees in dark
- Senses magic within sight
- Tentacles: targets grappled creature +5 D6 DC 13 CPM save or -1 on ability checks for 1 hour. Stacks.
```

### Flapper
A flying creature resembling a manta ray with a barbed tail and a wicked face.
```
Flapper, HP: 18(2d6+12), AC: 11, [All +1]
Bite/Tail +3 D6
Powers:
- Attach: DC 13 STR or grapple. It and attached split incoming damage
- Moan: DC 13 WIS save or -3 to all checks next turn. Save grants 1 day immunity
- Phantasms(1/day): Creates 3 illusory duplicates, disappear when hit
```

### Petri-chicken
A grey chicken-like creature 
```
Petra-chicken, HP: 1(D2), AC: 8, [All -1]
Peck +1 1 DC 12 CON this and next turn. Failing both results in petrification
```

### Hook-beak
An eye-less creature with long hooks on its arms
```
Vermin, HP: 54(6d6+36), AC: 13, [All +5]
Hook +5 D12
Powers:
- Echolocation sight
```

### Invisible Hunter
A creature summoned to track and kill a single target. 
```
Invisible Terror, HP: 18(2d6+12), AC: 11, [All +1]
Slam +3 D6
Powers:
- Always invisible
- Always knows general area of target while sharing plane
```

### Werewolf
```
Werewolf, HP: 27(3d6+18), AC: 12, [All +2]
Bite +4 D6: DC 12 CON save or curse with lycanthropy
Claws +4 D12
Spear +4 D4
Powers:
- Immune to non-magical or non-silvered damage
- Change between feral, hybrid, and humanoid form
```

Lycanthropy curse
```
DC 15 WIS save to avoid transforming under any of the following triggers:
- Fresh meat
- Blood
- Wounded animal
- Full moon
- Take damage
A success grants immunity for 1 hour.
When transformed into hybrid form use Werewolf stat block, controlled by keeper. Feasts and kills indiscriminantly. DC 20 WIS save to revert.
```

### Falsechest
```
Falsechest, HP: 9(D6+6), AC: 10, [All +0]
Bite +2 D4
Powers:
- Disguise: The falsechest can disguise as any object, allowing it to spring like a trap
- Tongue: DC 15 DEX check or creature if fused to falsechest's sticky tongue and the false chest deals bite damage. Check is automatically failed if creature touches disguised falsechest.
```

### Slime Cube
```
Vermin, Large, HP: 54(6d6+36), AC: 6, [All +5]
Acidic Pseudopod  +5 D6
Powers:
- Transparent: DC 14 WIS check to see creature is occupying a hallway
- Engulf: DC 15 STR save, captured creature takes D6 damage per turn
```

### Grey Slime
```
Grey Slime, HP: 9(D6+6), AC: 8, [All +0]
Acidic Pseudopod +2 D4
Powers:
- Amorphous: Can fit through 1-inch gaps
- Corrode: on hit, melee weapon takes permanent -1 damage penalty
- False appearance: DC 18 WIS check to distinguish grey slime from oily pool or wet rock
```

### Yellow Slime
```
Yellow Slime, Large, HP: 54(6d6+36), AC: 8, [All +3]
Acidic Pseudopod +2 D6
Powers:
- Amorphous: Can fit through 1-inch gaps
- Spider climb: Can climb upside-down or up vertical surfaces
- Split: If the slime has 10+ HP, it divides into two yellow slimes with half HP.
```

### Three-toed barbtooth
```
Vermin, HP: 54(6d6+36), AC: 13, [All +5]
Bite +5 D12
Tentacle +5 D6 auto-grapple
Power:
- Tentacle slam: grappled creature makes DC 14 CON save or takes D6 DMG and loses 2 actions on their next turn
```

### Beakbear
```
Vermin, HP: 27(3d6+18), AC: 12, [All +2]
Beak/Claws +4 D12
```

### Flamepede
```
Flamepede, large, HP: 54(6d6+36), AC: 13, [All +5]
Flaming Bite +5 D12
Powers:
- Heated Body: getting within 5ft deals D4 damage
```

### Rust Beast

```
Rust Beast, HP: 27(3d6+18), AC: 12, [All +2]
Bite +4 D12
Powers:
- Iron scent: Can smell iron within 30ft
- Rust metal: Metal melee weapons take -1 damage penalty when hit
- Antennae: Corrode one metal object within 5ft to rust powder
```

### Mesmer-beetle

```
Mesmer-beetle, HP: 54(6d6+36), AC: 13, [All +5]
Bite +5 D12
Powers:
- Tunnel 30ft
- Confusing gaze: DC 15 WIS save or confused. While confused D4
1-2: Does nothing
3: Moves thrice in random direction
4: Makes one attack against random creature
```

