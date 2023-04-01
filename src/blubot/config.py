# Config abstraction layer
import json
import sys

def load_json(path):
    with open(path, 'r') as file:
        json_obj = file.read()
        return json.loads(json_obj)

def load_hexes():
    return load_json('../../core_edition/campaigns/korsarus/hexes.json')