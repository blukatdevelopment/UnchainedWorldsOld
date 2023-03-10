import random

CONSONANTS = [
"g",
"k",
"t",
"h",
"n",
"l"]

VOWELS = ["ah",
"ee",
"ay",
"oh",
"oo",
"ih"]


def generate_name():
    name = ""
    for i in range(random.randint(3, 5)):
        name += random.choice(CONSONANTS)
        name += random.choice(VOWELS)
    return name

def main():
    for i in range(100):
        print(generate_name().capitalize())

main()