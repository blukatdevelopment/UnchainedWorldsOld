import random

EVIL_WORDS = [
"Zizar",
"shigara",
"floroso",
"sizhcozo",
"foaruso",
"zzzzozzzzz",
"pewop",
"fijej",
"tchtchtch",
"sapsapsim",
"harahimharhi"]

def generate_name():
    name = ""
    for i in range(3):
        name += random.choice(EVIL_WORDS)
    shuffled_characters = random.sample(name, len(name))
    random.shuffle(shuffled_characters)
    name = ''.join(shuffled_characters)
    start = 0
    end = random.randint(3, len(name))
    return name[start:end]

def main():
    for i in range(20):
        print(generate_name())


main()