import json


def open_file(path_to_file):
    with open(path_to_file) as file_json:
        return json.load(file_json)