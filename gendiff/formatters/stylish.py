def stylish(diff, depth=0):
    indent = ' ' * (depth * 4)
    lines = ['{']
    
    for key, value in diff.items():
        status = value["status"]
        if status == "added":
            lines.append(f"{indent}+ {key}: {value['value']}")
        elif status == "removed":
            lines.append(f"{indent}- {key}: {value['value']}")
        elif status == "unchanged":
            lines.append(f"{indent}  {key}: {value['value']}")
        elif status == "changed":
            lines.append(f"{indent}- {key}: {value['old']}")
            lines.append(f"{indent}+ {key}: {value['new']}")
        elif status == "nested":
            children = stylish(value["children"], depth + 1)
            lines.append(f"{indent}  {key}: {children}")
    
    lines.append(f"{indent}}}")
    return '\n'.join(lines)