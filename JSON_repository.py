import json


def push_json(name):
    with open('my_notes.json', 'w') as file:
        json.dump(name, file, indent=4)


def pull_json():
    with open('my_notes.json', 'r') as file:
        return json.load(file)
