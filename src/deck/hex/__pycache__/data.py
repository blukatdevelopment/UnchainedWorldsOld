ALPHA_NUM = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25
}


def load_json(path):
    with open(path, 'r') as file:
        json_obj = file.read()
        return json.loads(json_obj)

def load_hexes():
    return load_json('hexes.json')

def name_to_coords(name):
    x = name[1:]
    y_alpha = name[0:2]
    print(f"Coords, {name}, {y_alpha}, {x}")

def load_cells():
    hexes = load_hexes()
    cells = []
    for hx in hexes:
        coords = name_to_coords(name)
    return cells