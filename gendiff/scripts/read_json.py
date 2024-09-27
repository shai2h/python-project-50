import json


def open_json():
    with open('file1.json') as json_file:
        data_file_1 = json.load(json_file)
    return data_file_1
