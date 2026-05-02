def modify_file_content(path, content_to_append):
    with open(path, 'a') as file:
        file.write(content_to_append)