# Character Sheet
Here's an example sheet and a blank one.

## Example

Name: Velera the Trusted
[8, 8, 18, 12, 18, 18]
HP: 17/17
AC: 9
Perks: 5
Divine:
+4 to spellcasting
+2 CHA

Inventory: 8 Slots
1. Holy Book
2. Robes
3. 8 Incense Cubes
4. 16 Torches
5. waterskin
6. Dagger -1 D4
7.
8. Backpack:
    - 15 GP
    - 5 SP
    - Quill pen
    - Ink bottle

Divine Spells(Friff): spellcasting +8, spell DC 16
- Heal cloud(DC12): Creatures within one pace heal D6 HP.
- Enduring Smite(DC10): Touch melee weapon and the first hit from it within the next minute deals D6 extra damage.
- Detect Evil(DC10): Evil creatures(undead, fiends) within 6 paces show as aura for D6 turns.
- Resist Evil(DC10): Touch creature and it takes D6 less damage from the next evil(undead, fiend) creature's attack against it in the next minute.

```
# Rodbot macros. Modify, then run these to set up your character sheet
.clearrolls # Clears all existing macros
.saveroll str 1d20-3 # Strength
.saveroll dex 1d20-2 # Dexterity
.saveroll con 1d20+0 # Constitution
.saveroll int 1d20+1 # Intelligence
.saveroll wis 1d20+2 # Wisdom
.saveroll cha 1d20+3 # Charisma
.saveroll dagger 1d20-1 #to hit; 2d4kh1 # damage
.saveroll divine 1d20+3 #Spellcast roll; 12 # Spell DC
```

## Blank

Name:
[,,,,,]
HP: <CON score>/<CON score>
AC: 10+<DEX mod>
Perks:
Inventory: <STR score> slots