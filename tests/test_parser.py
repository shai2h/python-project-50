from gendiff.parsers import parser



def test_open_file_json():
    """
        Тест открытия json
    """
    path_to_file = 'gendiff/data/file1.json'
    assert parser.open_file(path_to_file)


def test_open_file_yaml():
    """
        Тест открытия yaml
    """
    path_to_file = 'gendiff/data/file1.yml'
    assert parser.open_file(path_to_file)