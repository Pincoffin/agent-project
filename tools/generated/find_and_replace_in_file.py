def find_and_replace_in_file(file_path, old_string, new_string):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        content = content.replace(old_string, new_string)
        with open(file_path, 'w') as file:
            file.write(content)
        return 'Replacement successful.'
    except Exception as e:
        return f'Error: {str(e)}'