def CalculateFileLines(**kwargs):
    path = kwargs.get('path', '')
    return count_lines_in_file(path)