import json
import yaml
    

def open_file(path_to_file):
    if path_to_file.endswith('.json'):
        with open(path_to_file) as file_json:
            return json.load(file_json)

    elif path_to_file.endswith('.yml') or path_to_file.endswith('.yaml'):
        with open(path_to_file) as file_yaml:
            return yaml.safe_load(file_yaml)

    else:
        raise ValueError('Неверный формат файла')
