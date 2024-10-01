import json


PATH_TO_FILE_ONE = 'gendiff\\data\\file1.json'
PATH_TO_FILE_SECOND = 'gendiff\\data\\file2.json'


def open_json():
    with open(PATH_TO_FILE_ONE) as json_file_one:
        data_file_one = json.load(json_file_one)

    with open(PATH_TO_FILE_SECOND) as json_file_two:
        data_file_two = json.load(json_file_two)
    return data_file_one, data_file_two
