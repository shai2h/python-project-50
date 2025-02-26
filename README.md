### Hexlet tests and linter status:
[![Actions Status](https://github.com/shai2h/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/shai2h/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/dca47f7c080aea2877cb/maintainability)](https://codeclimate.com/github/shai2h/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/dca47f7c080aea2877cb/test_coverage)](https://codeclimate.com/github/shai2h/python-project-50/test_coverage)

## Installation

1. **Make sure you have Python version 3.10 or higher installed.**
2. **Install Poetry (if not already installed):**  
   [Poetry Installation Guide](https://python-poetry.org/docs/#installation)
3. **Download the project's Wheel package:**
   ```bash
   poetry install dist/hexlet_code-0.1.0-py3-none-any.whl

## Dependencies

1. **Repository cloning**
    ```bash
    git clone git@github.com:shai2h/python-project-50.git

2. **Virtual environment**
    ```bash
    poetry shell

3. **Dependency installation**
    ```bash
    poetry install


## Usage examples:
1. **To get command help, use the following command:**
   ```bash
   poetry run gendiff -h
[![asciicast](https://asciinema.org/a/HgXxSHv03OOTQv8FtybmZdeRT.svg)](https://asciinema.org/a/HgXxSHv03OOTQv8FtybmZdeRT)

2. **To compare with the default 'stylish' format, use:**
   ```bash
   poetry run gendiff gendiff/data/file1.json gendiff/data/file2.json
[![asciicast](https://asciinema.org/a/8xMMfzjpBcVC6HSMpI4vLJihX.svg)](https://asciinema.org/a/8xMMfzjpBcVC6HSMpI4vLJihX)

3. **Usage with the --plain flag:**
    ```bash
   gendiff run -f plain gendiff/data/file1.yml gendiff/data/file2.json
[![asciicast](https://asciinema.org/a/yKsjRI9TrSOPz0lfMPh3paipL.svg)](https://asciinema.org/a/yKsjRI9TrSOPz0lfMPh3paipL)





