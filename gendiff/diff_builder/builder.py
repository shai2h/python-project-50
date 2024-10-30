def build_diff(data_one, data_two):
    result = {}
    all_keys = data_one.keys() | data_two.keys()

    for key in sorted(all_keys):
        if key not in data_one:
            result[key] = {"status": "added", "value": data_two[key]}
        elif key not in data_two:
            result[key] = {"status": "removed", "value": data_one[key]}
        elif isinstance(data_one[key], dict) and isinstance(data_two[key], dict):
            result[key] = {"status": "nested", "children": build_diff(data_one[key], data_two[key])}
        elif data_one[key] != data_two[key]:
            result[key] = {"status": "changed", "old": data_one[key], "new": data_two[key]}
        else:
            result[key] = {"status": "unchanged", "value": data_one[key]}
    return result