import json


PATH_TO_FILE_ONE = 'gendiff\\data\\file1.json'
PATH_TO_FILE_SECOND = 'gendiff\\data\\file2.json'

'''
Если ключ есть в обоих файлах, но значения отличаются — выводить оба значения (один с минусом, другой с плюсом).
Если ключ есть только в одном файле — выводить его со знаком "+" или "-" в зависимости от того, в каком файле он находится.
Если ключ есть в обоих файлах и значения одинаковы — выводить без изменений.
'''
def open_json():
    with open(PATH_TO_FILE_ONE) as json_file_one:
        data_file_one = json.load(json_file_one)

    with open(PATH_TO_FILE_SECOND) as json_file_two:
        data_file_two = json.load(json_file_two)

    result = {}

    for key, value in data_file_one.items():
        if key in data_file_two:
            # Если ключ есть в обоих файлах, но значения отличаются
            if value != data_file_two[key]:
                result[f'- {key}'] = value
                result[f'+ {key}'] = data_file_two[key]


            
    
    print(f'{data_file_one}\n{data_file_two}\n')
    
    return result





