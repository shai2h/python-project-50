from gendiff.utils import open_file


def gendiff_json_file(file_one, file_two):
    result = {}
    data_file_one, data_file_two = open_file(file_one), open_file(file_two)

    for key, value in data_file_one.items():
        if key in data_file_two:
            if value != data_file_two[key]:
                result[f'- {key}'] = value
                result[f'+ {key}'] = data_file_two[key]
            else:
                result[key] = value
        else:
            result[f'- {key}'] = value

    for key, value in data_file_two.items():
        if key not in data_file_one:
            result[f'+ {key}'] = value

    return dict(sorted(result.items(), key=lambda item: item[0].lstrip('+- ')))
