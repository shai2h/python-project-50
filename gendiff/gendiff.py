from gendiff.parsers import parser
from gendiff.formatters import stylish
from gendiff.diff_builder import builder


def generate_diff(file1, file2, format='stylish'):
    data1 = parser.open_file(file1)
    data2 = parser.open_file(file2)
    diff = builder.build_diff(data1, data2)

    if format == 'stylish':
        return stylish.stylish(diff)
    else:
        raise ValueError(f'Неверный формат {format}')


if __name__ == '__main__':
    print(generate_diff)