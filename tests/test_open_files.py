from gendiff.utils import open_file


def test_open_file_json():
    test_path = './gendiff/data/file1.json'
    loaded_data = open_file(test_path)
    test_path_data = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }

    assert loaded_data == test_path_data


def test_open_file_yaml():
    test_path = './gendiff/data/file1.yml'
    loaded_data = open_file(test_path)
    test_path_data = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }

    assert loaded_data == test_path_data