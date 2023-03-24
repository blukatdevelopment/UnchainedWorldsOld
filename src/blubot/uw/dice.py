import random
import re
import json

def roll_verbose(rollstring):
    elements = []
    for element in parse_elements(rollstring):
        elements = elements + roll_element(element)
    return {"elements": elements, "sum": get_sum(elements)}

def roll(rollstring):
    result = roll_verbose(rollstring)
    return result["sum"]

def roll_normal(mod):
    return roll("1d20") + int(mod)

def roll_advantage(mod):
    roll1 = roll_die(20)
    roll2 = roll_die(20)
    first_chosen = roll1 >= roll2
    highest = roll1 if first_chosen else roll2
    return {"sum": highest+mod, "roll1": {"sum": roll1, "dropped": not first_chosen}, "roll2": {"sum": roll2, "dropped": first_chosen}, "mod": mod}

def roll_disadvantage(mod):
    roll1 = roll_die(20)
    roll2 = roll_die(20)
    first_chosen = roll1 <= roll2
    lowest = roll1 if first_chosen else roll2
    return {"sum": lowest+mod, "roll1": {"sum": roll1, "dropped": not first_chosen}, "roll2": {"sum": roll2, "dropped": first_chosen}, "mod": mod}

def roll_attack(name, to_hit, damage, damage_type):
    attack1 = roll_normal(to_hit)
    attack2 = roll_normal(to_hit)
    damage1 = roll(damage)
    damage2 = roll(damage)
    to_hit_string = str(to_hit) if to_hit < 0 else "+" + str(to_hit)
    msg = f'1d20{to_hit_string} -> ({attack1}, {attack2})\n'
    msg += f'{damage} {damage_type} -> ({damage1}, {damage2})'
    return (msg, attack1, attack2, damage1, damage2)

def parse_elements(rollstring):
    rollstring = rollstring.replace(' ', '')
    pos_split = re.split('\+', rollstring)
    elements = []
    for element in pos_split:
        neg_split = re.split('\-', element)
        for i in range(len(neg_split)):
            elm = neg_split[i]
            if i > 0:
                elements.append("-" + elm)
            else:
                elements.append(elm)

    return elements

def roll_element(element):
    if 'd' not in element:
        return [{ "element": element, "result": int(element) }]
    parts = re.split('d', element)
    if len(parts) == 1:
        return [{"element": element, "result": roll_die(int(parts[0]))}]
    ret = []
    for i in range(int(parts[0])):
        ret.append({"element": f"d{parts[1]}", "result": roll_die(int(parts[1]))})
    return ret

def get_sum(elements):
    ret = 0
    for element in elements:
        ret += element["result"]
    return ret

def roll_die(size):
    return random.randint(1, size)

def is_this_a_unit_test():
    print(roll("1d20+5"))
    print(roll("1d20-1"))
    print(roll("2d20"))
    print(roll("1d4 + 2d6 + 3d12"))
    print(advantage(5))

#is_this_a_unit_test()