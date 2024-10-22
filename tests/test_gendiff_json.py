from gendiff.gendiff import gendiff_json_file


def test_gendiff_json():
    file_path_1 = 'gendiff/data/file1.json'
    file_path_2 = 'gendiff/data/file2.json'

    return_data = {
        '- follow': False,
        'host': 'hexlet.io',
        '- proxy': '123.234.53.22',
        '- timeout': 50,
        '+ timeout': 20,
        '+ verbose': True
    }

    assert return_data == gendiff_json_file(file_path_1, file_path_2)
