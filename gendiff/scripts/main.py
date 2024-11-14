import argparse
from gendiff.gendiff import generate_diff
from gendiff.formatters import stylish, plain


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument(
        'first_file',
        help='Path to the first configuration file'
    )
    parser.add_argument(
        'second_file',
        help='Path to the second configuration file'
    )
    parser.add_argument(
        '-f',
        '--format',
        help='set format of output (e.g., plain or json)',
        default='stylish'
    )
    args = parser.parse_args()


    diff = generate_diff(args.first_file, args.second_file, output_format=args.format)
    print(diff)

if __name__ == "__main__":
    main()
