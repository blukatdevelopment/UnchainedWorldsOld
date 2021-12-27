```
+------------------------------------------------------------------+
|  _____                       ___  ___          _                 |
| |  __ \                      |  \/  |         | |                |
| | |  \/ __ _ _ __ ___   ___  | .  . | __ _ ___| |_ ___ _ __ ___  |
| | | __ / _` | '_ ` _ \ / _ \ | |\/| |/ _` / __| __/ _ \ '__/ __| |
| | |_\ \ (_| | | | | | |  __/ | |  | | (_| \__ \ ||  __/ |  \__ \ |
|  \____/\__,_|_| |_| |_|\___| \_|  |_/\__,_|___/\__\___|_|  |___/ |
|                                                                  |
|                                                                  |
|  _____       _     _                                             |
| |  __ \     (_)   | |                                            |
| | |  \/_   _ _  __| | ___                                        |
| | | __| | | | |/ _` |/ _ \                                       |
| | |_\ \ |_| | | (_| |  __/                                       |
|  \____/\__,_|_|\__,_|\___|                                       |
|                                                                  |
+------------------------------------------------------------------+
```                 
# Preface

Oh, hey there! It's me, Blukat, your firendly neighborhood game master. I just
wanted to give a quick heads-up. My intent in writing a guide isn't to speak
authoritatively and create a relationship with this game where players and GMs
search for my social media activity to determine rulings. No, my goal is to
provide tools and perspectives that could be useful to GMs picking up this
system. My advice and tools will be limited by my experience, and my later self
will possibly find it necessary to rewrite this book from the ground up.

The Unchained Worlds system is intended as a system based in community content
creation, and as such, content creation will be included along with general
GM tools. If this is your first time GMing, I'll try to provide sufficient
definitions. So strap yourself in and enjoy the ride!

# Equipment

## Pen and paper
Physical paper is extremely versatile. You can draw a table, write a body of
text, and draw an illustration on the same page to your desired level of detail
without one iota of software. If character sheets don't have what you need,
you can make your own that looks just right. The main difficulty you'll
encounter with paper is organizing it. So, don't be afraid to organize your
paper in a binder, and to give each player their own binder with pockets full of
information that's used often as well as any campaign-specific information they
might frequently refer to. Maybe a world map? Definitely a couple pages of
blank paper for them to take notes with.

## Text
Text is the duct tape of information systems. No matter how pretty you can get
other formats of data (like save files for an application), text can fix
anything. It's versatile enough that you can do any facet of your DM prep using
only plain text files. It's also sturdy. Text editors rarely encounter the
kinds of technical issues more complicated systems do. Even when you use
automation for [Text art](https://patorjk.com/software/taag/), [Images](https://www.ascii-art-generator.org/),
[Tables](https://ozh.github.io/ascii-tables/), and [Graphs](https://asciiflow.com/#/),
you can make the same content by hand with enough patience. This means that if
such a tool should break or become unavailable, you can fix everything with
duct tape.

Can you make a character sheet this way? You betcha. Can you make stat blocks
for monsters? Most definitely. You can map out dungeons, store images as
ASCII art, and more!

## Battlegrid
Whether digital or physical, you'll get good mileage out of a battlegrid for
combats involving more than two or three enemies. Fish out a board from a game
of checkers or chess for a 40ftx40ft battlefield. You can also draw a grid on
a piece of posterboard or buy a plastic mat to write on with dry-erase markers.
Get creative! Most virtual tabletop systems will include a battlegrid to play
with as well.

## Virtual tabletop
Go do a search on the internet and you'll find a variety of competing products.
I'll recommend something like maptool or foundry VTT for Unchained Worlds. Each
has it's own user guide, so I'll end this section here.

# Common Tools
This section contains conceptual tools, abstractions that you can use 

## Embedded roll strings
Randomness makes everything better. Well, it can. And when you want
something to be more random, just chuck some random values in.
1d4 goblins are glaring at the party. Are there 1, or 4, or number
in the middle? You'll have to check to find out. It's important
to think through what the highest and lowest values will mean. If
the game would be brought to a halt by either, change the range (add a
modifier like +1 or -1), or maybe don't use a roll string here.

## Generalized Process

## Tables

### Simple tables
When you have a list of things to pick, and they all have the same
probability. Great for completely random things, like a random color
selection below.

```
+------+--------+
| Roll | Color  |
+------+--------+
|    1 | Red    |
|    2 | Green  |
|    3 | Blue   |
|    4 | Yellow |
+------+--------+
```

### DC Tables
These tables are to adjucate when a character attempts something, and their
modifier makes the task easier. The maximum value for these tables is
usually either 20 or 30, assuming bounded accuracy.

Here's an example of a table for pulling off a horse stunt.
```
+-------+------------------+
| Roll  |      Result      |
+-------+------------------+
| 1     | Broken bone      |
| 2-5   | Painful Wipeout  |
| 6-15  | Barely succeed   |
| 16-18 | Succeed easily   |
| 19-20 | Succeed in style |
+-------+------------------+
```

## Bell curve tables
2d6 is way different from 1d12. For one, it has 11 values, not 12. More importantly, there's not the same chance for every outcome. In fact, the closer
to the middle you get, the more likely it is you'll roll that outcome.
This is particularly useful when you want a list with certain options being
far more common than others.

## Hit Points

### Fuzzy Hitpoints
Monsters generally have a hit point formula and average value. You may choose
to track damage, rather than health. When your monster hits it's minimum hit
points worth of damage, but before it hits the max hit points worth of damage,
you can have wiggle room to let the monster die. This works well if you want
to introduce a bit more or less difficulty, allowing the party to either
get in an extra attack or a bility, or else to trade a defeat for a close call.
This is very much dice fudging.

### Hearts
Swap out your monster's hit points with some hearts and some arbitrary value
for how many hit points is in one heart. When your players make an attack
dealing enough to take out a heart, erase a heart. This reduces calculations
and reduces the effect of high-damage attacks, while increasing the effect of
low-damage attacks that are still larger than the heart size.

## Clocks

### Event Calendars
Want some random environmental detail?
Make a calendar, appropriate to your campaign (a couple months to a year is
common). You don't need to add an event to every day, but the following
information can make all the difference to making the world feel living and
breathing. You can generate these by hand with dice, or write a script.
Either way, keep track of the day as a number (from 1 to the last day in the
year) and have a lookup table to find information for the day.
- Day of the week - (to track weekly events like church, payday, weekend)
- Day of the month - (to track seasons)
- Lunar cycle (full moons, new moons, maybe even blue or blood moons)
- Weather (rain, flooding, wind, snow, cold, heat, dry streak)
- Holidays (who celebrates, what are they celebrating, how?)
- World events (science discovery, fashion trend, election)
- Plot events (big bad evil guy's plans advance, heists pulled off, assassinations)

### Progress Clocks
Draw a circle. Now draw some lines until you have N slices.
Every time X happens, color in one of the slices. When they are all
filled in, then Y happens. That's a progress clock.

Here's some examples:
Aggrevation clock, ticks when you annoy the NPC, when it's full they're done talking.
Interest clock, ticks when you make the NPC more interested in your timeshare
opportunity. When it's full, they're interested in meeting in a tavern and
discussing it at length(while the rest of the party ransacks the NPC's house).

Note that you could run two clocks at once. Maybe you want to convince the
NPC, but avoid annoying him.

Also works well as a doomsday counter for event-based plot arcs.

# Making Monsters

## What is a monster?
A monster's an excuse for your players to use all their characters' combat
abilities. They often provide an unambiguous evil, something that would make
the world safer or better if killed. Other times, they are merely dangerous
things that are better left alone and can be avoided. Lastly, people can fill
the role of monsters. There might not be anything monstrous about a commoner,
thief, or, guard, but they are combatants that can fight against the party
under certain circumstances.

A monster ideally provides a challenge to your party. A challenge that can be
instantly solved by expending class resources or using an abilities provides
player characters with a chance to be uniquely useful in a situation. Equally,
a challenge which cannot be instantly solved by abilities is a good way to test
the player's lateral thinking and provide some novelty. After fighting a novel
monster once, the players will know what to do with subsequent monsters of this
type and you can use that in your dungeon design.

## Archetypes
By shifting around stats, you'll often find monsters fitting into groups.

### Goon
Weak, frail, and numerous, goons are often either foot soldiers or part of a
hoard. Players will get a rush from being able to one-hit these creatures, but
they are not terribly interesting otherwise.

### Strikers
Your party may slowly chew away a bunch of goons. Throwing a striker in changes
that dynamic. A striker is a monster that is highly mobile, and which deals
higher damage than a goon. Archers, assassins, and creatures with stealth
abilities fit into this category well. These monsters will motivate your party
to prioritize them in favor of goons, and will.

### Glass Cannons
A glass cannon may be worse stat-wise than a goon in every way except firepower.
While they cannot take a beating, they sure can dish one out. They will be able
to deliver their damage from a distance, and are thus likely guarded by other
monsters.

### Tanks
Tanks absorb damage. Their regular damage should be higher than goons. Their
hit points, armor class, or both, will be boosted. A high AC ensures that the
creature cannot be easily felled by melee and ranged weapon attacks.

### Debuffer
A monster that can grapple, immobilize, or otherwise cause an effect on a target
presents a unique challenge. They will often have abilities that nullify the
abilities of the PCs, such as an anti-magic field, tentacles that prevent melee
attacks, or abilities that damage the target multiple rounds and challenges
concentration. It is often good to make whatever effects these monsters produce
end when said creature loses concentration or dies. This gives the party
a way to solve the problem introduced. Sometimes, however, you can make monsters
scary by giving them a debuff that can't easily be reversed, even after the
fight.

### Boss
Some monsters are intended to be a spectacle to fight. Bosses need to be able
to take hits. 


## Types
Monsters can come in a wide variety of forms, which each imply something about
them and their origins. Certain abilities and spells will interact with monsters
according to their type. Types are as follows:
- Aberration
- Beast
- Celestial
- Construct
- Dragon
- Elemental
- Fey
- Fiend
- Giant
- Humanoid
- Monstrosity
- Ooze
- Plant
- Undead

# Making spells and abilities

# Making Classes
So you're a player or new DM, and you have an idea that isn't covered by one of
the existing classes? Great! If you want, you can just stop at this sentence
and go write it. If you're still reading, then you are probably looking for
guidance. Let's get started.

## Foreword

### That's just, like, your opinion
Indeed! eVerything contained here is just a collection of opinions on making
content for the Unchained Worlds system. It's not canon, and shouldn't limit
any cool ideas you have. If you think your table would like content that
violates some law or guideline I give, do it! As long as you all have fun,
you're playing the game right.

### Learn the rules, then break them
Yes, you can ignore the advice I give. I recommend you only actually do that if
you feel you can make a case for doing so. I like to believe that my rules exist
for a reason. I also like to believe that there are exceptions to almost every
rule.

### Scale horizontally, not vertically
Wait, what does that mean? Well, it means that if you have an option to give
someone +2 intelligence, or a feat that lets them do some cool braniac thing,
players will 

## The top section of the character sheet

### A juicy description
Give us some flavor text describing your class, and what's cool about them.

### Proficiencies

#### Armor
What's the highest AC you want this class to have? Light will max out at 17,
same as medium. Plate will get you to 18. Regardless of these, shields will add
2. Armor's great for martial and half-casters, but I'd recommend against it
for full casters.

#### Weapons
Your players are likely to only use weapons they are proficient with, so pick
some weapons that you'd be comfortable seeing this class use. Bookworms might
have very few options, whereas martial classes might just have "simple weapons,
martial weapons" and call it a day.

#### Tools
Does your class require a tool(like an instrument or crafting tools) to operate?
Does being that class teach them cool stuff that others might not be familiar
with? If so, put it here.

#### Saving throws
Whatever the main ability is for your class, try and pick something else for
these. 

## The class table

### minimum experience
If you want to be on-par with the other classes, copy-paste their values.
In older TTRPGs certain classes were weaker, but leveled faster to compensate.
If you feel that's appropriate, apply it here.

### Hit Dice
The idea here is that a medium-sized humanoid isn't going to have more than
three hit dice. These dice start at 1d4 for a commoner, and max out at 1d12 for
some kind of tanky monstrosity. Full casters are almost always 1d4, half-casters
and skill monkey classes get a 1d6, and martial classes get a 1d8. 