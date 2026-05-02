def search_text_in_file(path, target_text):
    with open(path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines if target_text in line]