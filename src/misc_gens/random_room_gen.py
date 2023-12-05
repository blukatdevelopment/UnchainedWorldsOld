import random

CONTENT_TYPES = ["Social", "Monster", "Hazard", "Resource", "Anomaly", "Secret"]

def roll_d6():
    return random.randint(1, 6)

def roll_content():
    # Subtract because 0-indexed
    roll = roll_d6()-1 
    return CONTENT_TYPES[roll]

def roll_rooms(num_rooms, num_dice):
    for i in range(num_rooms):
        contents = []
        for j in range(num_dice):
            contents.append(roll_content())
        print("{}. {}".format(i+1, contents))

def main():
    roll_rooms(38, 3)

main()