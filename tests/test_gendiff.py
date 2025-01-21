from gendiff.gendiff import generate_diff


def test_generate_diff_stylish():
    file1 = "gendiff/data/file1.json"
    file2 = "gendiff/data/file2.json"
    expected_output_file = "tests/fixtures/expected_stylish.txt"

    with open(expected_output_file, 'r', encoding='utf-8') as f:
        expected = f.read().strip()

    result = generate_diff(file1, file2, "stylish")

    print("Результат функции:")
    print(result)
    print("Ожидаемый результат:")
    print(expected)
    assert result == expected


def test_generate_diff_plain():
    file1 = "gendiff/data/file1.yml"
    file2 = "gendiff/data/file2.yml"
    expected_output_file = "tests/fixtures/expected_plain.txt"
    
    with open(expected_output_file, 'r', encoding='utf-8') as f:
        expected = f.read().strip()

    result = generate_diff(file1, file2, "plain")
    assert result == expected

def test_generate_diff_json():
    file1 = "gendiff/data/file1.json"
    file2 = "gendiff/data/file2.json"
    expected_output_file = "tests/fixtures/expected_json.json"
    
    with open(expected_output_file, 'r', encoding='utf-8') as f:
        expected = f.read().strip()

    result = generate_diff(file1, file2, "json")
    assert result == expected

