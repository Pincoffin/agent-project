
def summarize_file(path):
    try:
        with open(path, 'r') as file:
            content = file.read()
            return summarize_text(content)
    except FileNotFoundError:
        return "File not found."
