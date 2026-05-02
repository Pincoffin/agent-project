def count_lines_in_file(path):
    with open(path, 'r') as file:
        return sum(1 for line in file)