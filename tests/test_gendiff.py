from gendiff.gendiff import generate_diff



def test_generate_diff_stylish():
    file1 = "./gendiff/data/file1.json"
    file2 = "./gendiff/data/file2.json"

    # Ожидаемый результат
    expected_result = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: None
      + setting4: blah blah
      + setting5: {
              key5: value5
        }
        setting6: {
            doge: {
              - wow:
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
              key: value
        }
      + nest: str
    }
  - group2: {
          abc: 12345
          deep: {
              id: 45
        }
    }
  + group3: {
          deep: {
              id: {
                  number: 45
            }
        }
          fee: 100500
    }
}"""

    # Получаем реальный результат
    result = generate_diff(file1, file2, "stylish").strip()

    # Сравниваем результат с ожидаемым
    assert result == expected_result.strip()


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

