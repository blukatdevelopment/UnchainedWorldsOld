# This is a script to simulate selecting perks for a character

import random

B_BOOL = 0
B_INT = 1


def roll_2d6():
    return random.randint(1, 6) + random.randint(1, 6)

def blank_character():
    return {}

def unarmed_perk(num_perks):

    b_types = [B_BOOL, B_INT, B_INT, B_INT, B_INT, B_INT]
    b_vals = roll_benefits(num_perks, b_types)

    output = "\nUnarmed Perk:{}{}".format(num_perks, b_vals)

    if b_vals[0] == True:
        output += "\n\tA successful stunt may deal unarmed damage"
    if b_vals[1] > 0:
        output += "\n\tUnarmed attacks deal {}d2 damage".format(b_vals[1]+1)
    if b_vals[2] > 0:
        output += "\n\t+{} to unarmed attacks".format(b_vals[2])
    if b_vals[3] > 0:
        output += "\n\t({})+2 to either STR, DEX, or CON, or +1 to two".format(b_vals[3])
    if b_vals[4] > 0:
        output += "\n\t{}/rest, deal double maximum damage".format(b_vals[4])
    if b_vals[5] == True:
        output += "\n\tNo penalty on second or third unarmed attack"
    return output

def martial_perk(num_perks):
    b_types = [B_BOOL, B_INT, B_INT, B_INT, B_INT, B_INT]
    b_vals = roll_benefits(num_perks, b_types)

    output = "\nMartial Weapons Perk:{}{}".format(num_perks, b_vals)

    if b_vals[0] == True:
        output += "\n\tTwo-handed attacks deal D10 damage"
    if b_vals[1] > 0:
        output += "\n\t{}/rest, perform stunt as part of attack".format(b_vals[1])
    if b_vals[2] > 0:
        output += "\n\t{}/rest, add a D6 to martial damage".format(b_vals[2])
    if b_vals[3] > 0:
        output += "\n\t+{} to martial weapon attacks".format(b_vals[3])
    if b_vals[4] > 0:
        output += "\n\t({})+2 to either STR or CON, or +1 to both".format(b_vals[4])
    if b_vals[5] == True:
        output += "\n\tFree attack if a melee attack misses you"
    return output

def great_perk(num_perks):
    b_types = [B_BOOL, B_INT, B_INT, B_INT, B_INT, B_INT]
    b_vals = roll_benefits(num_perks, b_types)

    output = "\nGreat Weapons Perk:{}{}".format(num_perks, b_vals)

    if b_vals[0] == True:
        output += "\n\tDeal max damage when you have less than half your maximum HP"
    if b_vals[1] > 0:
        output += "\n\t+{} to great weapon attacks".format(b_vals[1])
    if b_vals[2] > 0:
        output += "\n\t{}/rest, deal max damage".format(b_vals[2])
    if b_vals[3] > 0:
        output += "\n\t({})+2 to either STR or CON, or +1 to both".format(b_vals[3])
    if b_vals[4] > 0:
        output += "\n\t{}/rest, automatically hit".format(b_vals[4])
    if b_vals[5] == True:
        output += "\n\tMay reroll great weapon damage, using second roll"
    return output

def ranged_perk(num_perks):
    b_types = [B_BOOL, B_INT, B_INT, B_INT, B_INT, B_INT]
    b_vals = roll_benefits(num_perks, b_types)

    output = "\nRanged Weapons Perk:{}{}".format(num_perks, b_vals)

    if b_vals[0] == True:
        output += "\n\tPower up ensures max damage for a ranged attack"
    if b_vals[1] > 0:
        output += "\n\t+{} to ranged weapon attacks".format(b_vals[1])
    if b_vals[2] > 0:
        output += "\n\t{}/rest, add D6 to ranged damage".format(b_vals[2])
    if b_vals[3] > 0:
        output += "\n\t({})+2 to either DEX or WIS, or +1 to both".format(b_vals[3])
    if b_vals[4] > 0:
        output += "\n\t{}/rest, add D6 to ranged attack roll".format(b_vals[4])
    if b_vals[5] == True:
        output += "\n\tSecond attack with ranged has no penalty"
    return output

def minor_perk(num_perks):
    b_types = [B_BOOL, B_INT, B_INT, B_INT, B_INT, B_INT]
    b_vals = roll_benefits(num_perks, b_types)

    output = "\nMinor Weapons Perk:{}{}".format(num_perks, b_vals)

    if b_vals[0] == True:
        output += "\n\tDual-wielding deals 2d4 damage"
    if b_vals[1] > 0:
        output += "\n\t{}/rest, deal max minor weapon damage".format(b_vals[1])
    if b_vals[2] > 0:
        output += "\n\t+{} to minor weapon attacks".format(b_vals[2])
    if b_vals[3] > 0:
        output += "\n\t{}/rest, add a D6 to minor weapon damage".format(b_vals[3])
    if b_vals[4] > 0:
        output += "\n\t({})+2 to either STR, DEX, or CON, or +1 to two".format(b_vals[4])
    if b_vals[5] == True:
        output += "\n\tSecond attack with minor weapon has no penalty"
    return output

def defense_perk(num_perks):
    b_types = [B_INT, B_INT, B_INT, B_INT, B_INT, B_INT]
    b_vals = roll_benefits(num_perks, b_types)

    output = "\nDefense Perk:{}{}".format(num_perks, b_vals)

    if b_vals[0] > 0:
        output += "\n\t{}/rest, spend 10 minutes to restore D4 HP".format(b_vals[0])
    if b_vals[1] > 0:
        output += "\n\t{}/rest gain D6 THP that lasts 1 hour".format(b_vals[1])
    if b_vals[2] > 0:
        output += "\n\tGain +{} to max HP".format(b_vals[2])
    if b_vals[3] > 0:
        output += "\n\t({})+2 to STR, DEX, or CON, or +1 to two".format(b_vals[3])
    if b_vals[4] > 0:
        output += "\n\t{}/rest, take half damage for D6 turns".format(b_vals[4])
    if b_vals[5] > 0:
        output += "\n\t+{} to AC when wearing heavy armor".format(b_vals[5])
    return output


def roll_benefits(n, b_types):
    # Roll the benefits for n perks
    # Reroll when a non-stacking benefit is rolled two or more times
    b_vals = []
    for b_type in b_types:
        if b_type == B_BOOL:
            b_vals.append(False)
        else:
            b_vals.append(0)
    i = 0
    while i < n:
        roll = roll_2d6()
        if roll == 2:
            if b_types[0] == B_BOOL:
                if b_vals[0] == True:
                    i -= 1
                else:
                    b_vals[0] = True
            else:
                b_vals[0] += 1
        elif roll == 4:
            if b_types[1] == B_BOOL:
                if b_vals[1] == True:
                    i -= 1
                else:
                    b_vals[1] = True
            else:
                b_vals[1] += 1
        elif roll <= 7:
            if b_types[2] == B_BOOL:
                if b_vals[2] == True:
                    i -= 1
                else:
                    b_vals[2] = True
            else:
                b_vals[2] += 1
        elif roll <= 9:
            if b_types[3] == B_BOOL:
                if b_vals[3] == True:
                    i -= 1
                else:
                    b_vals[3] = True
            else:
                b_vals[3] += 1
        elif roll <= 11:
            if b_types[4] == B_BOOL:
                if b_vals[4] == True:
                    i -= 1
                else:
                    b_vals[4] = True
            else:
                b_vals[4] += 1
        else:
            if b_types[5] == B_BOOL:
                if b_vals[5] == True:
                    i -= 1
                else:
                    b_vals[5] = True
            else:
                b_vals[5] += 1
        i += 1
    return b_vals


def main():
    character = "\n\nDefense Expert:"
    character += defense_perk(20)
    print(character)

    character = "\n\nPugilism Expert:"
    character += unarmed_perk(20)
    print(character)

    character = "\n\nAxe Expert:"
    character += minor_perk(20)
    print(character)

    character = "\n\nSword Expert:"
    character += martial_perk(20)
    print(character)

    character = "\n\nGreatsword Expert:"
    character += great_perk(20)
    print(character)

    character = "\n\nBow Expert:"
    character += ranged_perk(20)
    print(character)

main()