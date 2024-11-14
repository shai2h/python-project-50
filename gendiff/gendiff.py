from gendiff.parsers import parser
from gendiff.formatters import stylish
from gendiff.diff_builder import builder
from gendiff.formatters import plain

def generate_diff(file1, file2, output_format='stylish'):
    data1 = parser.open_file(file1)
    data2 = parser.open_file(file2)
    diff = builder.build_diff(data1, data2)

    if output_format == 'stylish':
        return stylish.stylish(diff)
    elif output_format == 'plain':
        return plain.plain(diff)
    else:
        raise ValueError(f'Неверный формат {output_format}')


if __name__ == '__main__':
    from gendiff import main
    main()