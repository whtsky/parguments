def count_indentation(lines):
    if not isinstance(lines, (list, tuple)):
        lines = lines.splitlines()
    indentations = []
    for line in lines:
        if not line.strip(' '):
            continue
        indentations.append(len(line) - len(line.lstrip(' ')))
    return min(indentations)


def remove_indentation(lines):
    if not isinstance(lines, (list, tuple)):
        lines = lines.splitlines()
    i = count_indentation(lines)
    return "\n".join([line[i:] if len(line) > i else "" for line in lines])
