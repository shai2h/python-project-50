import json


def json_format(diff):
    """
    На вход получает словарь различий

    Возвращает форматированный json
    """
    return json.dumps(diff, indent=4)
