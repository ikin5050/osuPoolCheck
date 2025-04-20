import json

def load_database(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)
