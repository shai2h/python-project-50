def inner(diff, path=""):
    lines = []

    for key, value in sorted(diff.items()):
        full_path = f"{path}.{key}" if path else key
        status = value['status']

        if status == 'added':
            lines.append(
                f"Property '{full_path}' was added with value: {format_value(value['value'])}"
            )
        elif status == "removed":
            lines.append(f"Property '{full_path}' was removed")
        elif status == "changed":
            old_value = format_value(value["old"])
            new_value = format_value(value["new"])
            lines.append(f"Property '{full_path}' was updated. From {old_value} to {new_value}")
        elif status == "nested":
            lines.extend(inner(value["children"], full_path))
    return lines

def plain(diff):
    return '\n'.join(inner(diff))

def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    return str(value)
