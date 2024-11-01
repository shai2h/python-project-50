def stylish(diff, depth=1):
    indent = ' ' * (depth * 4 - 2)
    lines = ['{']
    
    for key, value in diff.items():
        status = value["status"]
        if status == "added":
            formatted_value = format_value(value['value'], depth + 1)
            lines.append(f"{indent}+ {key}: {formatted_value}")
        elif status == "removed":
            formatted_value = format_value(value['value'], depth + 1)
            lines.append(f"{indent}- {key}: {formatted_value}")
        elif status == "unchanged":
            formatted_value = format_value(value['value'], depth + 1)
            lines.append(f"{indent}  {key}: {formatted_value}")
        elif status == "changed":
            old_value = format_value(value['old'], depth + 1)
            new_value = format_value(value['new'], depth + 1)
            lines.append(f"{indent}- {key}: {old_value}")
            lines.append(f"{indent}+ {key}: {new_value}")
        elif status == "nested":
            children = stylish(value["children"], depth + 1)
            lines.append(f"{indent}  {key}: {children}")
    
    lines.append(' ' * ((depth - 1) * 4) + '}')
    return '\n'.join(lines)

def format_value(value, depth):
    if isinstance(value, dict):
        nested_lines = ['{']
        indent = ' ' * (depth * 4)
        for k, v in value.items():
            nested_lines.append(f"{indent}  {k}: {format_value(v, depth + 1)}")
        nested_lines.append(' ' * ((depth - 1) * 4) + '}')
        return '\n'.join(nested_lines)
    return str(value).lower() if isinstance(value, bool) else value
