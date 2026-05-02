def FilterLinesByLength(min_length, **kwargs):
    path = kwargs.get('path', '')
    with open(path, 'r') as file:
        lines = file.readlines()
    filtered_lines = [line for line in lines if len(line.strip()) >= min_length]
    return ''.join(filtered_lines)