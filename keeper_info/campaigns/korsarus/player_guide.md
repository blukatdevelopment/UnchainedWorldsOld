# Quickstart Guide
## What kind of campaign is this?

### The original character
In some campaigns, each player takes a few hours or days crafting and refining a fleshed-out character with a backstory that can be woven into the narrative of the campaign. Let's call these original characters, or OCs. OCs offer players a great deal of creative freedom to express their character concepts. An OC might have a gimmic like using a teapot to cast their spells, be an incarnation of a character from a book/anime/cartoon, or act as a self-insert that uniquely represents the player's identity. These characters can have a pre-destined "character arc", or a series of changes in the character that will provide dramatic tension across a linear campaign.  For the Korsarus campaign, we won't be bringing fully-formed characters like this to insert into the world.

### Why not OCs?
There are a few reasons why OCs aren't a good fit for this campaign:
- Tone clash: Your pigfolk character named "Kris P. Bacon" is silly and delightful. That said, the intent for this campaign is a mundane/boring/believable baseline that gives room for a range of horror/comedy/absurdity/wonder/drama to unfold depending on what happens.
- Worldbuilding: A lot of the world is shrouded in mystery, and that leaves little material to create fully fleshed-out backstories whole cloth.
- Investment: players are attached to their OCs before they arrive at the table, making any legitimate danger seem more punishing.
- Homework: An OC is made by a single author alone. This prevents the rest of the table from participating or getting invested in the your character. 

### The discovered character
So what do we do instead?
- Simple concept: A profession and a reason for adventuring will get you a lot further than you may suspect.
- Use the table: Can't think of a detail? Relate your character with the others. 
- Play your backstory: Is your character a blank slate? Good. Let's fill it up with some formative experiences. Let your first few relationships and hard decisions define your character. If you and a group are feeling adventurous, ask to play in a starter session, a high-stakes and dramatically intense scenario that will result in particularly exotic backstories.



## Your first character
Your first character starts as a Commoner from the Soot culture. This will get you into the action quickly. As you interact with the world, you'll unlock new classes, cultures, and other character options. When you unlock your first class, you may immediately give them a level in this class and update their ability scores using the rules described in the `Your other characters` section.

### Your Appearance
Your appearance can be your choice of human or beast folk, as described below.

#### Human
Humans are the most common humanoid by far, and they vary heavily. While some humans stand eight feet in height, and others stand under four, it's most common for humans to sand between five and six feet tall. Rarely, humans have elongated ears, or those of a beast coupled with a similar tail. The most common complexion for human ranges from pink, yellow, tan, and brown. Green, blue, and crimson skin is exotic, but not unheard of. Humans were originally created by the god Bimros in an attempt to populate the world with worshippers.

#### Beast folk
Beast have a vaguely humanoid frame, but their features are that of beasts. Fur, scales, feathers, and leathery hides are the norm for beast folk. They were originally the creation of the god Uaos, who envied the creation of humans and wanted his own worshippers.

### Your backstory
You were born and raised in the filthy slums of the copper ring of Korsarus City. Whether your old life involved shoveling manure, begging on the street, or picking pockets, one truth remains. You've got nothing to show for that life, and nothing to lose by abandoning it for a life of adventuring. For the first time in your life, you are ready to plunge head-first into danger, even if it means abandoning the protection of Korsarus's outer-most walls.

![Korsarus City](https://raw.githubusercontent.com/blukatdevelopment/UnchainedWorlds/main/keeper_info/campaigns/korsarus/korsarus_city.png "Korsarus City")

### Your name
Follow this process and you'll get a proper Soot name.
1. Think up words that describe your character's job or appearance. An older dairy farmer might have: cow, rain, bowl, and beard.
2. Stick them together in one word. Example: Cowrainbowlbeard
3. Strategically slice off some syllables. Coanboward
4. Slice it into a first and last name. Coan Boward

### Your stat block
To get you started quickly, don't worry about building a stat block. A stat block has been provided below.
You can use Blubot's `/character update` command and use this stat block to create a character. You'll want to change the name from "Fresh Meat", though.
```
{
"name": "Fresh Meat",
"xp": 0,
"ac": 10,
"hp": 4,
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

### Character thread
Add a comment to `#characters` with your character name. Then create a thread for them and post your stat block in it. You can use the Example character as reference, except that you won't need to post standard array or roll abilities yet.

### Using Blubot
- `/character update` updates a character, or creates one if no character with that name exists. 
- `/character active` tells you which character is currently active
- `/character set` sets your active character
- `/character list` lists your characters
- `/character get` gives you the specified character's json
- `/character delete` deletes the specified character
- `/check` rolls an ability or skill check twice. The first value is used unless advantage or disadvantage applies to the roll.
- `/attack list` shows what attacks your character has
- `/attack use` makes an attack
- `/status display` shows your character's status
- `/status clear` clears their status to full HP/THP/stamina
- `/status hp` change your hit points. Negative is damage, positive is healing. THP is automatically consumed before HP.
- `/status thp` change the amount of thp you have. Positive adds, negative removes.
- `/status stamina` change the number of stamina dice you have. Positive adds, negative substracts.

## Your other characters
After you've made your first character, you'll generate ability scores, choose a culture, and then choose a class. Ask, and you can get help generating names for other cultures.

### Ability Scores
You get a choice. You can either use the standard array, or roll scores.

#### Standard Array
This is the consistent option that works well if you know what class you'd like to pick, as you'll have the same values to work with. `[15, 14, 13, 12, 10, 8]` You may assign these ability scores in your preferred order.

#### Roll Scores
Get ready to discover your character! Use rodbot's `!roll stats`

### Pick a culture
Select a culture, either Soot, or another you have unlocked.

### Pick a class
Select a class, either Commoner, or another you have unlocked.

### Create your stat block with the Blubot character page
You can enter your character details. The page will generate a blob of JSON for you. You can feed this to Blubot using the `/character update` command.

### Character thread
Add a comment to `#characters` with your character name. Then create a thread for them and post your stat block in it. If you're rolling ability scores, do it there with the `.roll abilities` command using rodbot.

## Content guide

### [Core Rules]()
These spell out how to play the base game, minus classes, cultures, etc.

### [Cultures](https://homebrewery.naturalcrit.com/share/4XnPfJgwGg-x)
Culture roughly describes the norms you were raised under. Within any culture, there's a range of variation from the given norms.

#### Gold Robes
A wealthy people left over from the aristocracy of the empire of man. They have rich taste and wear robes with gold woven into the hem.

#### The Silent
A people so dedicated to protecting the lost secrets of Titan technology that they cut their own tongues out and speak with their hands.

#### Bronzehammers
A people obsessed with a mystical affinity for metal. Each family maintains a hammer with the full lineage inscribed.

#### Coggers
A people concerned with scientific innovation that have great reverance for tiny folk.

#### Soot
A people which provide the labor needed to propel industrial expansion.

#### Field Folk
Aggrarians who enjoy the peaceful life of villages and small towns, and who have an affinity for giant folk, who often act as their protectors.

#### Deep Folk
Living without the sun off of subterranean life, the deep folk are greatly hospitable to those they meet.

#### Wild Folk
A king's worst nightmare: wild folk are obsessed with dismantling structures of authority and are never far when a revolution occurs.

#### Greenfoot
Those who retreat from industry and attempt to live in harmony with nature, under the protection of the Fey.

#### Wayfarers
A people of travelers who share their special interests and eclectic hoards of knowledge with the world one city at a time.

### Classes
Many classes offer one distinct archetype, while some provide feats from a list, and others are broken into subclasses.

#### [Commoner](https://homebrewery.naturalcrit.com/share/RhYcMMb8EvnP)
The starter class that prepares you to feel very powerful playing any of the others.

#### [Warrior](https://homebrewery.naturalcrit.com/share/-_W1rK4UofP-)
You are physically tough and ferocious, and these qualities make you an excellent martial combatant.

#### [Thief](https://homebrewery.naturalcrit.com/share/FrO7KSCugh9w)
What you lack in sturdyness or ferocity, you make up for with flexibility and stealth.

#### [Runesmith](https://homebrewery.naturalcrit.com/share/96GH7In3kzLe)
You understand magic as a language that can be written on runestones and archived in books.

#### [Diviner](https://homebrewery.naturalcrit.com/share/RcgnErV5EpEs)
Good and bad deeds result in gaining and losing piety, which is the power source for your divine spellcasting.

#### [Monk](https://homebrewery.naturalcrit.com/share/eKHZbW1PXwG-)
Channel your ki to unlock your full martial prowess and shift between defense, offense, and mobility.

#### [Muse](https://homebrewery.naturalcrit.com/share/VIKSSJTBb32O)
Your free spirit channels magic through self expression, and draws from a broad knowledge of the world.

#### [Psion](https://homebrewery.naturalcrit.com/share/gub183ljMrOh)
You appear to be a commoner, that is, until you levitate a mounted knight off the ground or make someone's heart explode.

#### [Alchemist](https://homebrewery.naturalcrit.com/share/g-G93wNSTafk)
Cook up and bank potions from random tables.

#### [Gunsmith](https://homebrewery.naturalcrit.com/share/XTEiRuRNHnhB)
There are few who can command thunder from metal quite like you.

#### [Werewolf](https://homebrewery.naturalcrit.com/share/PbDFUd-rHUjJ)
Control the terrible might of your werewolf form, or become lost in it's bloodlust.

#### [Scientist](https://homebrewery.naturalcrit.com/share/S8XV09PemJoj)
You wield the fruits of a curious and creative mind, assembling contraptions which rival magic.

#### [Shaman](https://homebrewery.naturalcrit.com/share/YG2dg5FTIy9u)
You channel the power of nature through your relationship with a nature spirit, wielding it's magic and transforming into beasts.

#### [Soul Forger](https://homebrewery.naturalcrit.com/share/eiLYilzETVWn)
With your infuser, you fill soul stones and forge fiendish minions.

### [Spells](https://homebrewery.naturalcrit.com/share/MgUX9_p_7q6x)
Spells are grouped up by level. Control + F is going to be your friend here if you're looking for a specific one.